# pip install falsk-wtf : 플라스크에서 폼 관리하는 기능
    # CSRF 보호 정책 설정
    # 쉽고 유연한 폼 적용하여 유효성 검증, input 태그 생성


from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from fileinfo import info
import os

UPLOAD_FOLDER = './uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_CONTENT_LENGTH'] = 1024 * 1024 * 5
app.config['SECRET_KEY'] = 'abc' # CSRF 보호 정책 설정을 하려면 필요

class FileForm(FlaskForm):
    files = FileField('파일', validators=[FileRequired()]) # 업로드한 파일 객체

@app.route('/', methods=['GET', 'POST']) # type: ignore
def index():
    form = FileForm()
    if form.validate_on_submit(): # 폼 데이터가 유효한지(POST 요청이 유효하게 들어왔는지) 체크
        file = form.files.data # 업로드한 파일 객체
        safe_filename = secure_filename(file.filename)
        file.save(UPLOAD_FOLDER + safe_filename)
        ctime, mtime, atime, size = info(safe_filename)
        return render_template('check.html',
                               fileinfo = {'ctime':ctime,
                                           'size':size})
    else: # GET방식이거나 POST요청이 유효하지 않을경우
        return render_template('upload.html', form=form) # upload.html 수정
    
if __name__ == '__main__':  
    app.run(debug=True) 