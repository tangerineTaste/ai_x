from flask import Flask, url_for, render_template

app = Flask(__name__)
# 라우팅 : URL을 특정함수(뷰함수)에 연결하는 작업

@app.route('/') # static Route
def hello():
    return render_template('06_index.html')

@app.route("/profile/<name>/<int:age>")
def get_profile(name, age):
    return render_template("06_profile.html",
                           name=name,
                           age=age)
if __name__ == '__main__':
    with app.test_request_context():
        print('hello 뷰함수의 요청경로 :', url_for('hello'))
        print(url_for('get_profile', name='sim', age=33))
    app.run(debug=True, port=80)