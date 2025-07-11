from flask import Flask

from predict import loaded_model, predict_apt_price

application = Flask(__name__) # 웹 어플리케이션 객체 생성

@application.route('/')
def handller_function():
    return '<h1>Hello, Flask!</h1>'

# /apt/2005/106/8
@application.route('/apt/<year>/<square>/<floor>')
def aptPredictHandler(year, square, floor):
    result = predict_apt_price(year, square, floor)
    return '<h1>예측 금액은 {}원 입니다</h1>'.format(result)

if __name__ == "__main__":
    application.run()