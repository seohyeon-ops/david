from flask import Flask, render_template
import socket   # 내 컴퓨터의 이름을 가져오기 위해 모듈 추가

app = Flask(__name__)

@app.route('/')
def index():
    # 코드 추가
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    # render_templates에 computername 인자를 포함
    return render_template('index.html', computername=hostname)

@app.route('/test2')
def test2():
    return 'This is test2'

# /menu 라우트
@app.route('/menu')
def menu():
    return render_template('menu.html') 

if __name__ == '__main__':
    app.run(debug=True)  # debug 모드라 코드가 수정될 때 자동 수정,if 조건이 작동함
