from flask import Flask, request, redirect, render_template, url_for, send_file, flash
from flask_pymongo import PyMongo
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session security

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

class UserForm(FlaskForm):
    name = StringField('Name', validators=[validators.InputRequired()])
    age = IntegerField('Age', validators=[validators.InputRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[validators.InputRequired()])
    number = StringField('Phone Number', validators=[validators.InputRequired(), validators.Length(min=10, max=10)])
    email = StringField('Email', validators=[validators.InputRequired(), validators.Email()])
    # Add validation for other questions if needed

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
    form = UserForm()
    return render_template('quiz.html', form=form)

@app.route('/loader')
def loader():
    return render_template('loader.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/submit', methods=['POST'])
def submit():
    form = UserForm(request.form)
    if form.validate():
        try:
            user = User(
                name=form.name.data,
                age=form.age.data,
                gender=form.gender.data,
                number=form.number.data,
                email=form.email.data,
                # Add other questions from the form if needed
            )
            user_data = user.__dict__
            mongo.db.users.insert_one(user_data)
            return redirect('/loader')
        except Exception as e:
            flash('An error occurred while processing your request.')
            return redirect(url_for('quiz'))
    else:
        flash('Please fill out all required fields correctly.')
        return redirect(url_for('quiz'))

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
