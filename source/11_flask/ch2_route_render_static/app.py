from flask import Flask

app = Flask(__name__) # 앱 인스턴스 생성

@app.route('/') # @ : 데코레이터를 통해 요청가능한 URL등록
def main_handler():
    return "<h1>Hello, World</h1>"

# 파일명이 app.py 라면 실행은 flask run 입력시 자동 실행. 그래서 파일명을 app이라고 지정해야 함
# flask run --debug --port=80 : 포트번호 80에서 실행 가능
# 파일명이 app.py 가 아니라면
if __name__ == '__main__':
    app.run(debug=True, port=80)