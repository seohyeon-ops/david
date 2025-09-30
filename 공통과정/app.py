from flask import Flask, render_template
import socket   # socket 모듈 추가

app = Flask(__name__)

@app.route('/')
def index():
    # hostname 값 설정
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    # index.html 템플릿에 computername 값 전달
    return render_template('index.html', computername=hostname)

# /menu 라우트
@app.route('/menu')
def menu():
    return render_template('menu.html') 

if __name__ == '__main__':
    app.run(debug=True)  