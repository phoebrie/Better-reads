import sqlite3
from flask import Flask, render_template
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