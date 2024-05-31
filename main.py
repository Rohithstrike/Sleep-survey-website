from flask import Flask, request, redirect, render_template, url_for, send_file
from flask_pymongo import PyMongo
import csv
import os
from bson import ObjectId

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://rohith3085:rohith_db_5803@cluster0.a9hpefq.mongodb.net/user_info?retryWrites=true&w=majority&tlsInsecure=true"
mongo = PyMongo(app)

# Database Model equivalent for MongoDB
class User:
    def __init__(self, name, age, gender, number, email, question1, question2, question3, question4, question5, question6,
                 question7, question8, question9, question10, question11, question12, question13, question14, question15,
                 question16, question17, question18, question19):
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/loader')
def loader():
    return render_template('loader.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit', methods=['POST'])
def submit():
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
        user_data = user.__dict__
        mongo.db.users.insert_one(user_data)
        return redirect('/loader')
    except Exception as e:
        return str(e), 500

@app.route('/export-csv', methods=['GET'])
def export_csv():
    try:
        query = mongo.db.users.find()
        csv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'users.csv')
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ["_id", "name", "age", "gender", "number", "email", "question1", "question2", "question3", "question4", 
                      "question5", "question6", "question7", "question8", "question9", "question10", "question11", 
                      "question12", "question13", "question14", "question15", "question16", "question17", "question18", 
                      "question19"]
            writer.writerow(header)
            for user in query:
                row = [str(user.get(column, "")) for column in header]
                writer.writerow(row)
        return send_file(csv_path, as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
