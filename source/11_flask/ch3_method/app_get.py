from flask import Flask, render_template, request, abort
from models import Member

app = Flask(__name__)

@app.template_filter('mask_pw')
def mask_password(password):
    return "*" * len(password)

@app.route("/user/<name>")
def viewFunction(name):
    return f"<h1>{name}님 환영합니다</h1>"

@app.route('/user')
def user():
    name = request.args.get('name')
    if name:
        return "<h1>전달받은 파라미터 이름 : {name}님</h1>"
    else:
        abort(404)

@app.errorhandler(404)
def error_handler(error):
    return render_template('404_pageNotFound.html'), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/join_form', methods=['GET'])
def join_form():
    return render_template('1_onlyget/join.html')

@app.route('/join', methods=['GET'])
def join():
    name = request.args.get('name')
    id = request.args.get('id')
    pw = request.args.get('pw')
    addr = request.args.get('addr')
    member = Member(name,id,pw,addr)
    return render_template('result.html', member=member)


if __name__ == '__main__':
    app.run(port=80)