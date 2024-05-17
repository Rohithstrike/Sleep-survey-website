from flask import Flask, request, redirect, render_template, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
import shutil
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Get the absolute path to the directory of the current file
basedir = os.path.abspath(os.path.dirname(__file__))

# Determine the database path based on the environment
if os.getenv('VERCEL_ENV'):
    src_database_path = os.path.join(basedir, 'user_info.db')
    dest_database_path = "/tmp/user_info.db"
    
    # Copy the database file to /tmp if it doesn't already exist
    if not os.path.exists(dest_database_path):
        shutil.copyfile(src_database_path, dest_database_path)
    
    db_path = dest_database_path
    print(f"Database path on Vercel: {db_path}")
else:
    db_path = os.path.join(basedir, 'user_info.db')
    print(f"Database path locally: {db_path}")

# Configure Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define your database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    number = db.Column(db.String(15))
    email = db.Column(db.String(120))
    question1 = db.Column(db.Integer)
    question2 = db.Column(db.Integer)
    question3 = db.Column(db.Integer)
    question4 = db.Column(db.Integer)
    question5 = db.Column(db.Integer)
    question6 = db.Column(db.Integer)
    question7 = db.Column(db.Integer)
    question8 = db.Column(db.Integer)
    question9 = db.Column(db.Integer)
    question10 = db.Column(db.Integer)
    question11 = db.Column(db.Integer)
    question12 = db.Column(db.Integer)
    question13 = db.Column(db.Integer)
    question14 = db.Column(db.Integer)
    question15 = db.Column(db.Integer)
    question16 = db.Column(db.Integer)
    question17 = db.Column(db.Integer)
    question18 = db.Column(db.Integer)
    question19 = db.Column(db.Integer)

    def __init__(self, name, age, gender, number, email, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19):
        self.name = name
        self.age = age
        self.gender = gender
        self.number = number
        self.email = email
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
        self.question6 = question6
        self.question7 = question7
        self.question8 = question8
        self.question9 = question9
        self.question10 = question10
        self.question11 = question11
        self.question12 = question12
        self.question13 = question13
        self.question14 = question14
        self.question15 = question15
        self.question16 = question16
        self.question17 = question17
        self.question18 = question18
        self.question19 = question19

# Create tables if they do not exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:
            user = User(
                name=request.form['name'],
                age=request.form['age'],
                gender=request.form['gender'],
                number=request.form['number'],
                email=request.form['email'],
                question1=request.form['question1'],
                question2=request.form['question2'],
                question3=request.form['question3'],
                question4=request.form['question4'],
                question5=request.form['question5'],
                question6=request.form['question6'],
                question7=request.form['question7'],
                question8=request.form['question8'],
                question9=request.form['question9'],
                question10=request.form['question10'],
                question11=request.form['question11'],
                question12=request.form['question12'],
                question13=request.form['question13'],
                question14=request.form['question14'],
                question15=request.form['question15'],
                question16=request.form['question16'],
                question17=request.form['question17'],
                question18=request.form['question18'],
                question19=request.form['question19']
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
