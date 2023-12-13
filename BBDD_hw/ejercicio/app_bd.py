import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

# 0.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    conex=sqlite3.connect('books.db')
    cur=conex.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conex.close()
    return jsonify({'books': books})

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
@app.route('/v0/sorted_books', methods=['GET'])
def sorted_books():
    conex=sqlite3.connect('books.db')
    cur=conex.cursor()
    sorted_b=cur.execute("SELECT * FROM books ORDER BY author DESC")
    conex.close()
    return jsonify({'sorted books': sorted_b})

# 2.Ruta para obtener los libros de un autor como argumento en la llamada
@app.route('/v0/<string:author', methods=['GET'])
def author_books(author):
    conex=sqlite3.connect('books.db')
    cur=conex.cursor()
    result=cur.execute("SELECT * FROM books WHERE author = ?",(author,))
    results=result.fetchall()
    conex.close()
    return jsonify({'author books': results})

# 3.Ruta para obtener los libros filtrados por título, publicación y autor
@app.route('/v0/filtered', methods=['GET'])
def books_filtered():
    conex = sqlite3.connect("books.db")
    cur = conex.cursor()
    title = request.args['title']
    published = request.args['published']
    author = request.args['author']
    cur.execute('''SELECT * FROM books WHERE title = ? AND published = ? AND author = ?''', (title, published, author ,))
    books_filter = cur.fetchall()
    conex.close()
    return jsonify(books_filter)
app.run()