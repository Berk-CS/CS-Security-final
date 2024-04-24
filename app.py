from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    url = request.form['url']
    username = request.form.get('username')
    password = request.form.get('password')

    session = requests.Session()
    if username and password:
        # Perform login with credentials
        login_data = {
            'username': username,
            'password': password
        }
        response = session.post(url, data=login_data)
    else:
        # Perform login without credentials
        response = session.get(url)

    # Check if login was successful
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return f'Logged in successfully to {title}'
    else:
        return 'Login failed'

if __name__ == '__main__':
    app.run(debug=True)