from flask import Flask, render_template, request, flash, redirect, url_for
from . import utils, database, models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = database.query_db('SELECT * FROM users WHERE username = ?', [username], one=True)
        if user is None:
            flash('User does not exist')
            return redirect(url_for('login'))
        elif not utils.check_password_hash(user['password'], password):
            flash('Incorrect password')
            return redirect(url_for('login'))
        else:
            flash('Logged in successfully')
            return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    utils.logout_user()
    flash('Logged out successfully')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not utils.username_exists(username):
            database.query_db('INSERT INTO users (username, password) VALUES (?, ?)', [username, utils.generate_password_hash(password)])
            flash('Registered successfully')
            return redirect(url_for('login'))
        else:
            flash('Username already exists')
            return redirect(url_for('register'))
    else:
        return render_template('register.html')