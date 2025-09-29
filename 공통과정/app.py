from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"   # 기본 경로(/)에서 "Hello World!" 출력

# 추가한 부분
@app.route('/menu')
def menu():
    return render_template('menu.html')  # /menu 접속 시 menu.html 보여줌

if __name__ == '__main__':
    app.run(debug=True)  # Flask 서버 실행
