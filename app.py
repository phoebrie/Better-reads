import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_review(review_id):
    conn = get_db_connection()
    review = conn.execute('SELECT * FROM REVIEWS WHERE id = ?', (review_id,)).fetchone()
    conn.close()
    if review is None:
        abort(404)
    return review

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bn?cxghaz;z07A6eu'


@app.route('/')
def index():
    conn = get_db_connection()
    reviews = conn.execute('SELECT * FROM reviews').fetchall()
    conn.close()
    return render_template('index.html', reviews=reviews)

@app.route('/<int:review_id>')
def review(review_id):
    review = get_review(review_id)
    return render_template('review.html', review=review)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO reviews (title, author, rating, content) VALUES (?,?,?,?)', (title, author, rating, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('create.html')