from flask import Flask, render_template, request, redirect, session
import json
import os
import sys

app = Flask(__name__)
app.secret_key = 'supersecretctfkey'

# Usage: python app.py bank1  (will use accounts1.json and news1.json)
if len(sys.argv) > 1:
    bank = sys.argv[1]
    ACCOUNTS_FILE = os.path.join(os.path.dirname(__file__), f'accounts{bank[-1]}.json')
    NEWS_FILE = os.path.join(os.path.dirname(__file__), f'news{bank[-1]}.json')
    CHAT_FILE = os.path.join(os.path.dirname(__file__), f'chat{bank[-1]}.json')


def load_accounts():
    with open(ACCOUNTS_FILE, 'r') as f:
        return json.load(f)

def get_accounts():
    return load_accounts()

def load_news():
    if not os.path.exists(NEWS_FILE):
        return []
    with open(NEWS_FILE, 'r') as f:
        return json.load(f)

def load_chat():
    if not os.path.exists(CHAT_FILE):
        return []
    with open(CHAT_FILE, 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    accounts = get_accounts()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in accounts and password == 'password123':
            session['user'] = username
            return redirect('/news')
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/news')
def news():
    if 'user' not in session:
        return redirect('/login')
    accounts = get_accounts()
    account = accounts[session['user']]
    news_items = load_news()
    return render_template('news.html', user=session['user'], account_id=account['account_id'], news_items=news_items)

@app.route('/account')
def account():
    if 'user' not in session:
        return redirect('/login')
    accounts = get_accounts()
    requested_id = request.args.get('account_id')
    for username, data in accounts.items():
        if str(data['account_id']) == requested_id:
            return render_template('account.html', owner=username, balance=data['balance'], flag=data['flag'])
    # Custom humorous error page
    return render_template('error.html', message="Oops! This account doesn't exist.<br><br>Hacking banks is illegal.<br>🫵🏼 <br>You have been reported to the authorities? "), 404

@app.route('/chat')
def chat():
    if 'user' not in session:
        return redirect('/login')
    chat_messages = load_chat()
    return render_template('chat.html', chat_messages=chat_messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

