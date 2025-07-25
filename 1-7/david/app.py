
from flask import Flask, render_template,request
from gtts import gTTS  
import base64 
import io 

app = Flask(__name__) 
@app.route('/',methods=['GET','POST']) 
def index():
    error = None 
    audio = None 

    if request.method == 'POST':
        input_text = request.form.get('input_text', '').strip()
        lang = request.form.get('lang', 'ko')

        if not input_text:  ## 아무것도 안 썼거나 이상한 언어가 들어오면 에러 메시지
            error = '입력된 텍스트가 없습니다.'
        elif lang not in ['ko', 'en', 'ja', 'es']:
            error = f'지원하지 않는 언어입니다: {lang}'
        else: ## 정상이면 음성 변환 실행
            try:
                tts = gTTS(text=input_text, lang=lang)  
                mp3_fp = io.BytesIO() 
                tts.write_to_fp(mp3_fp) 
                mp3_fp.seek(0)
                audio = base64.b64encode(mp3_fp.read()).decode('utf-8') 
            
            except Exception as e:
                error = f'TTS 변환 실패: {str(e)}'
    
    return render_template('index.html', error=error, audio=audio)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 


# GET과 POST란? (HTML에서 데이터를 주고받는 방식)
# : 웹페이지에서는 브라우저(사용자)와 서버(Flask 같은 백엔드)가 서로 정보를 주고 받을 필요가 있음

# GET 방식: 처음 페이지 접속 -> 폼만 보여줌(보여주기만 하면 됨)
# POST 방식: 폼이 제출된 경우 -> 데이터 처리(데이터를 서버로 보냄)


