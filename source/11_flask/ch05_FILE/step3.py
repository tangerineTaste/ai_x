# step3 : 파일첨부화면 + 첨부했던 파일 목록 (다운로드 + 삭제)
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from fileinfo import info
import os
from flask import send_file # 다운로드 시 필요한 모듈
from flask import redirect, url_for # 삭제 후 '/' 요청결로로 리다이렉트

UPLOAD_FOLDER = './uploads/'

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
        # 업로드 폴더의 파일 정보를 listup
        filelist = os.listdir(UPLOAD_FOLDER)
        infos = [] # 파일 정보(파일명, 파일생성시점, 파일최종수정시잠, 파일크기) 리스트
        for filename in filelist:
            ctime, mtime, atime, size = info(filename)
            fileinfo = {'name': filename,
                        'create':ctime,
                        'modify':mtime,
                        'size':size}
            infos.append(fileinfo)
        return render_template('home.html', form=form, infos=infos) # upload.html 수정 

@app.route('/delete/<filename>') # type: ignore
def delete(filename):
    os.remove(UPLOAD_FOLDER + filename)
    return redirect(url_for('index'))

@app.route('/download/<filename>') # type: ignore
def download(filename):
    return send_file(UPLOAD_FOLDER + filename,
                     as_attachment=True) # 브라우저로 파일이 열리지 않고 다운로드만 가능

if __name__ == '__main__':  
    app.run(debug=True) 