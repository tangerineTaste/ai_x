import joblib
from sympy.plotting.intervalmath import floor

# 가상환경 만들기 : python -m venv .venv
# 가상환경 들어가기 : .venv\Scripts\activate
# python -m pip install --upgrade pip
# pip install statsmodels
# pip install joblib
# pip install xlwings
# pip install flask

loaded_model = joblib.load('../model/ex1_apt_price_regression.joblib')

def predict_apt_price(year, square, floor):
    input_data = [[int(year), int(square), int(floor), 1]]
    pred = round(loaded_model.predict(input_data)[0]*10000)
    return format(pred, ',') + '원'

if __name__ == '__main__':
    year = input('연도 : ')
    square = input('제곱미터 : ')
    floor = input('층 수 : ')
    print('예측 가격 :',predict_apt_price(year,square,floor))
