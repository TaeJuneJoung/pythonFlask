import random
from flask import Flask, render_template, request
#render_template을 import하고 templates라는 폴더에서 'render_template("html_file.html")'을 통해 받음

app = Flask(__name__)

@app.route("/")
def hello():
    return '<img src="https://t1.daumcdn.net/cfile/tistory/220FC13A5293933A11">'
    
@app.route("/html_tag")
def html_tag():
    # span은 연결되는걸 아시겠죠?!
    return '''
    <h1>자동완성이 되지 않으니 불편하구만</h1>
    <img src="https://t1.daumcdn.net/cfile/tistory/220FC13A5293933A11">
    <h2>그래도 밥은 먹었으니...<h2>
    <span>Span이 어떤 형식인지 보시게나</span>
    
    <span>바로 확인하세요</span>
    <p>p의 차이도 봐야하지 않겠어요?</p>
    <p>확인하셔야죠</p>
    '''
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", data=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    return render_template("cube.html", num=num, data=num*num*num)#파이썬에서는 **기능으로 제곱기능이 있다. num**3이면 num의 3제곱
    
@app.route("/lunch")
def lunch():
    #점심메뉴를 추천해주는 코드를 작성
    menu = ['짜장면','짬뽕','고기','샤브샤브']
    data = random.choice(menu)
    return render_template("run.html", data=data)
    
@app.route("/lotto")
def lotto():
    data = random.sample(range(1,46),7)
    data = sorted(data)
    return render_template("run.html", data=data)
    
@app.route("/form")
def form():
    return render_template("form.html")