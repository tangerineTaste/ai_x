from flask import Flask, request, render_template
from flask import redirect, url_for, abort # redirect, 강제로 예외 발생
from flask import session # 로그인/로그아웃
from models import TodoRequest

app = Flask(__name__)
# app.secret_key = '안녕하세요'
app.config['SECRET_KEY'] = 'abc123'

todo_data = {
  1 : {
    'id': 1,
    'content': 'flask 공부',
    'is_done': True,
  },
  2 : {
    'id': 2,
    'content': 'django 공부',
    'is_done': False,
  },
}

@app.route('/')
def index():
    '로그인 성공 로직(세션의 로그인 한 사람의 정보 넣기) /todos로 리다리엑트'
    session['user_id'] = 'hong'
    session['username'] = '홍길동'
    return redirect(url_for('todos'))

@app.route('/logout')
def logout():
    '세션의 값을 삭제하고 /todos로 리다리엑트'
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect(url_for('todos'))

@app.route('/todos')
def todos():
    'todo 데이터를 리스트로 변환하여 렌더링'
    ret = list(todo_data.values()) # 딕셔너리 리스트로
    order = request.args.get('order', 'asc') # 정렬 순서
    if order == 'desc':
        ret = ret[::-1]
    next_id = max(todo_data.keys()) + 1 if len(todo_data) > 0 else 1
    return render_template('todo/todos.html', 
                           todos=ret,
                           next_id = next_id,
                           order=order)

@app.route('/create', methods=['POST'])
def create():
    '새로운 할일(request.form)을 추가하는 로직'
    print(request.form.to_dict())
    todo = TodoRequest(**request.form.to_dict()) # type: ignore
    todo_data[todo.id] = todo.model_dump()
    return redirect(url_for('todos'))
    

@app.route('/todos/<int:id>')
def todo(id):
    '해당 id의 todo_data를 html로 렌더링'
    todo = todo_data.get(id)
    if todo:
        return render_template('todo/todo.html', todo=todo)
    return abort(404, description='해당 id의 todo를 찾을 수 없습니다.')

@app.route('/update/<int:id>') # 수정할 수 있는 페이지
def update(id):
    '수정할 수 있는 페이지로 가기'
    return render_template('todo/update.html', todo=todo_data.get(id))

@app.errorhandler(404)
def not_found(error):
    return render_template('page_not_found.html', error=error), 404

@app.route('/update/<int:id>/<string:content>/<string:is_done>', methods=['PUT'])
def get_update(id, content, is_done):
    todo = todo_data.get(id)
    if todo:
        todo['content'] = content
        todo['is_done'] = is_done
        todo_data[id] = todo
        return f'수정 완료. {todo["content"]}'
    return abort(404, description='해당 id의 todo를 찾을 수 없습니다.')

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    todo = todo_data.get(id)
    if todo:
        del todo_data[id]
        return f'삭제 완료. {todo["content"]}'
    return abort(404, description='해당 id의 todo를 찾을 수 없습니다.')

if __name__ == '__main__':    
    app.run(debug=True)

