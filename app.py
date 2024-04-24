from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Perform GET request
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
            login_status = f'Logged in successfully to {title}'
        else:
            login_status = 'Login failed'

        # Security Scanner
        scanner_result = security_scanner(url)
        
        return render_template('index.html', login_status=login_status, scanner_result=scanner_result)

    return render_template('index.html', login_status=None, scanner_result=None)

def security_scanner(url):
    attempts = 5  # Number of random username-password combinations to attempt
    success_count = 0
    session = requests.Session()

    for _ in range(attempts):
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        login_data = {
            'username': username,
            'password': password
        }

        response = session.post(url, data=login_data)
        if response.ok:
            success_count += 1

    return f'Successful login attempts: {success_count}/{attempts}'

if __name__ == '__main__':
    app.run(debug=True)
