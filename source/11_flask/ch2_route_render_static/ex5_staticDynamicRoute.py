from flask import Flask, url_for

app = Flask(__name__)
# 라우팅 : URL을 특정함수(뷰함수)에 연결하는 작업

@app.route('/') # static Route
def hello():
    return '<h1>Hello</h1>'

@app.route('/profile/<name>/<age>') # dynamic Route
def get_profile(name, age):
    return '<h1>profile : {}님 {}살입니다.</h1>'.format(name,age)

if __name__ == '__main__':
    # 플라스크가 http요청 관련 정보를 활성화하여 정보 출력
    with app.test_request_context():
        print('hello 뷰함수의 요청경로 :', url_for('hello'))
        print(url_for('get_profile', name='sim', age=33))
    app.run(debug=True, port=80)
    print('run')