 Sleep Survey Website

 Welcome to the Sleep Survey Website repository! This project aims to understand and improve sleep quality through comprehensive surveys and insightful data analysis. 
 Built with a modern tech stack, our website provides a seamless and interactive user experience.

 Key Features

User-Friendly Interface: Designed with HTML, CSS, and JavaScript for a clean and intuitive user experience.
Responsive Design: Fully responsive, ensuring smooth operation across all devices.
Interactive Surveys: Engaging and straightforward surveys to collect valuable sleep data.
Secure Data Storage: MongoDB is used to securely store survey data, ensuring privacy and data integrity.
Data Analysis & Insights: Python Flask processes and analyzes responses to provide meaningful insights and recommendations.
Real-Time Feedback: Immediate tips and feedback based on survey results to help users improve their sleep quality.

Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Python Flask
Database: MongoDB

Getting Started

Follow these steps to set up the project locally:

Clone the repository:

git clone https://github.com/Rohithstrike/Sleep-survey-website.git

cd sleep-survey-website

Create and activate a virtual environment:

Mac and Linux:

python3 -m venv env
source env/bin/activate

Windows:

python -m venv env
.\env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Install MongoDB:

Windows:

Download the MongoDB installer from the official website.
Follow the installation steps, making sure to select "Complete" when asked for the setup type.
After installation, add MongoDB to the system PATH.
Start MongoDB by running mongod in the Command Prompt.

Mac:

Install Homebrew if you haven't already:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install MongoDB:

brew tap mongodb/brew
brew install mongodb-community@5.0

Start MongoDB:

brew services start mongodb/brew/mongodb-community

Linux:

Import the public key used by the package management system:

wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

Create a list file for MongoDB:

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

Reload the local package database:

sudo apt-get update

Install the MongoDB packages:

sudo apt-get install -y mongodb-org

Start MongoDB:

sudo systemctl start mongod

Optionally, ensure that MongoDB will start following a system reboot:

sudo systemctl enable mongod

Set up MongoDB configuration:

Ensure you have MongoDB running.
Update the database configuration in config.py.

Run the Flask application:

Mac and Linux and Windows:

python3 main.py

Open your browser:
Navigate to http://localhost:5000 to access the Sleep Survey Website.

Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

