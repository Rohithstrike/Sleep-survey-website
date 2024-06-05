from flask import Flask, request, redirect, render_template, send_from_directory, url_for
from pymongo import MongoClient
from bson import ObjectId
import csv
import os

app = Flask(__name__)

# MongoDB Atlas configuration with the new URI and password
mongo_uri = 'mongodb+srv://rohith3085:GvCwJOd45rjkWANH@cluster0.hjin0iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
db = client['Know-your-sleep-genetics']  # Use the correct case-sensitive database name
users_collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ZG93bmxvYWR0aGVjc3Y=')
def download():
    return render_template('ZG93bmxvYWR0aGVjc3Y=.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/thankyou')
def thankyou():
    user_id = request.args.get('user_id')
    if user_id:
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
            return render_template('thankyou.html', user=user)
    return 'User not found', 404

def calculate_sum_of_questions(form_data):
    question_keys = [f'question{i}' for i in range(1, 20)]
    total_sum = sum(int(form_data.get(key, 0)) for key in question_keys)
    return total_sum

@app.route('/loader')
def loader():
    user_id = request.args.get('user_id')
    return render_template('loader.html', user_id=user_id)


@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = request.form
        total_sum = calculate_sum_of_questions(form_data)
        user = {
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'number': request.form['number'],
            'email': request.form['email'],
            'question1': request.form['question1'],
            'question2': request.form['question2'],
            'question3': request.form['question3'],
            'question4': request.form['question4'],
            'question5': request.form['question5'],
            'question6': request.form['question6'],
            'question7': request.form['question7'],
            'question8': request.form['question8'],
            'question9': request.form['question9'],
            'question10': request.form['question10'],
            'question11': request.form['question11'],
            'question12': request.form['question12'],
            'question13': request.form['question13'],
            'question14': request.form['question14'],
            'question15': request.form['question15'],
            'question16': request.form['question16'],
            'question17': request.form['question17'],
            'question18': request.form['question18'],
            'question19': request.form['question19'],
            'total_sum': total_sum
<<<<<<< HEAD
            
=======
>>>>>>> origin/main
        }
        result = users_collection.insert_one(user)
        return redirect(url_for('loader', user_id=str(result.inserted_id)))
    except Exception as e:
        return str(e), 500

@app.route('/export-csv', methods=['GET'])
def export_csv():
    try:
        users = list(users_collection.find())
        csv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'users.csv')
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['name', 'age', 'gender', 'number', 'email', 'question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8', 'question9', 'question10', 'question11', 'question12', 'question13', 'question14', 'question15', 'question16', 'question17', 'question18', 'question19','total_sum']
            writer.writerow(header)
            for user in users:
                row = [user.get(col, '') for col in header]
                writer.writerow(row)
        return send_from_directory(directory=os.path.abspath(os.path.dirname(__file__)), path='users.csv', as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)