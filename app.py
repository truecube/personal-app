from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'Prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://truecube:CalbAgus1@localhost/personal-app'
else: 
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zeoqncqkibfzks:ff108000cb33ea47c4a5811bfe884824eb22b84398a203cac91aca9224576f21@ec2-52-23-40-80.compute-1.amazonaws.com:5432/dhplfpbr7md2p'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    
    email = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))
    dateOfBirth = db.Column(db.DateTime())
    favoriteColor = db.Column(db.String(20))
    hobby = db.Column(db.String(200))

    def __init__(self, email, password, dateOfBirth, favoriteColor, hobby): 
        self.email = email
        self.password = password
        self.dateOfBirth = dateOfBirth
        self.favoriteColor = favoriteColor
        self.hobby = hobby

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup(): 
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login(): 
    email = request.form['email']
    password = request.form['password']
    print(email, password)
    user = User.query.filter_by(email=email, password=password).first()
    if user is None: 
        return render_template('login.html', message='Wrong credentials. Please try again')
    else: 
        return render_template('welcome.html', user=user)

@app.route('/createAccount', methods=['POST'])
def createAccount(): 
    email = request.form['email']
    password = request.form['password']
    dateOfBirth = request.form['dateOfBirth']
    hobby = request.form['hobby']
    color = request.form['color']
    print(email, password, dateOfBirth, hobby, color)
    message = "You have successfully created an account. You can login now"
    if(db.session.query(User).filter(User.email == email).count() == 0): 
        data = User(email, password, dateOfBirth, color, hobby)
        db.session.add(data)
        db.session.commit()
    else: 
        message = "Problem creating user as the account already exists"    
    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run()