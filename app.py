from flask import Flask, request, render_template, redirect, session, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Default dictionary of usernames and passwords (you can replace this with your own)
user_pass_dict = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
    
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        username = request.form.get('username')
        password = request.form.get('password')

        # Store the values in session
        session['url'] = url
        session['username'] = username
        session['password'] = password

        return redirect(url_for('actions'))

    return render_template('index.html')

@app.route('/actions', methods=['GET', 'POST'])
def actions():
    url = session.get('url')

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'Check Login':
            # Attempt login using GET request
            success = attempt_login(url)
            return f"Login attempt using GET request: {'Success' if success else 'Failure'}"

        elif action == 'Check Dictionary Login':
            # Attempt login using a dictionary of usernames and passwords
            success = attempt_dict_login(url, user_pass_dict)            
            return f"Login attempt using dictionary: {'Success' if success else 'Failure'}"

    return render_template('actions.html')

def attempt_login(url):
    # Perform login attempt using GET request
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def attempt_dict_login(url, user_pass_dict):
    # Attempt login using a dictionary of usernames and passwords
    for user, pwd in user_pass_dict.items():
        try:
            response = requests.get(url, auth=(user, pwd))
            if response.status_code == 200:
                return True  # Return True immediately upon successful login
        except:
            pass  # Ignore exceptions and continue trying other credentials
    return False  # Return False if no successful login attempt was made

if __name__ == '__main__':
    app.run(debug=True)
