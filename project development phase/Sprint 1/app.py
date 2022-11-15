from flask import Flask,render_template,request, redirect,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['POST','GET'])
def login():
    return render_template('login.html' ,msg="success")

@app.route('/forgot', methods=['POST','GET'])
def forgot():
    return render_template('forgot.html' ,msg="success")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__=='__main__':
    app.run(debug=True)

       