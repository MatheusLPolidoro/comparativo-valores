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
    quantity = request.form['quantity']

    if query.strip() == "":
        message = "Por favor, digite o item que deseja buscar!"
        message_type = "error"
        return render_template('index.html', message=message, message_type=message_type)
    if not quantity.isdigit() or int(quantity) < 10 or int(quantity) > 100:
        message = "Por favor, digite uma quantidade de itens entre 10 e 100!"
        message_type = "error"
        return render_template('index.html', message=message, message_type=message_type)

    python_path = r'C:\Users\badi_\Documents\comparativo-valores\env\Scripts\python.exe'
    subprocess.run([python_path, 'app/scraping/scraper.py', query, quantity])
    database = "database/database.db"
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT title, price, link, reviews, discount FROM products")
    results = cur.fetchall()
    if results:
        message = "Busca realizada com sucesso!"
        message_type = "success"
    else:
        message = "Nenhum resultado encontrado!"
        message_type = "error"
    return render_template('index.html', results=results, message=message, message_type=message_type)