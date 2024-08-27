from flask import Flask, render_template, request, redirect, url_for, session
from book_database import BookDatabase
from user_database import UserDatabase

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random string

book_db = BookDatabase()
user_db = UserDatabase()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_db.add_user(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('register.html', error='Username already exists')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if user_db.authenticate(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('query', '')
    results = book_db.search(query)
    return render_template('search.html', results=results, query=query)

@app.route('/library')
def library():
    if 'username' not in session:
        return redirect(url_for('login'))
    user_books = user_db.get_user_books(session['username'])
    return render_template('library.html', books=user_books)

@app.route('/purchase/<int:book_id>')
def purchase(book_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    book = book_db.get_book(book_id)
    if book and user_db.purchase_book(session['username'], book):
        return redirect(url_for('library'))
    else:
        return redirect(url_for('search'))

if __name__ == '__main__':
    app.run(debug=True)