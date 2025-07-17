from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        no = None
    elif request.method == 'POST':
        no = request.form['no']
    return render_template('quiz.html', no=no)

if __name__ == '__main__':
    app.run(debug=True)