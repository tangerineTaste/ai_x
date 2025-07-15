# app.py
from flask import Flask, render_template, request, redirect, url_for
from filters import mask_password
from models import Member

app = Flask(__name__)

app.template_filter('mask_pw')(mask_password)

@app.errorhandler(404)
def errorhandler(error):
    return render_template('2_postetc/404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return render_template('2_postetc/index.html')

@app.route('/join', methods=['GET', 'POST']) # type: ignore
def join():
    if request.method == 'GET':
        return render_template('2_postetc/join.html')
    elif request.method == 'POST':
        member = Member(**request.form.to_dict()) # type: ignore
        return render_template('2_postetc/result.html', member=member) 
    
@app.route("/update/<name>/<id>/<pw>/<addr>", methods=["PATCH"])
def update(name, id, pw, addr):
    return f"{name}님의 정보를 수정하였습니다." 

if __name__ == '__main__':
    app.run()