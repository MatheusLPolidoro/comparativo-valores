from app import app
from flask import request, render_template
import subprocess
import sqlite3
from app.scraping.database import create_connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    python_path = r'C:\Users\badi_\Documents\comparativo-valores\env\Scripts\python.exe'
    subprocess.run([python_path, 'app/scraping/scraper.py', query])
    database = "database/database.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT title, price, link, reviews, discount FROM products")
    results = cur.fetchall()
    return render_template('index.html', results=results)