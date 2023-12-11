from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My first API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return jsonify(books)
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/v0/book_id', methods=['GET'])
def book_id():
    id=int(request.args['id'])
    results=[book for book in books if book['id']==id]
    return results
    #copiado, no hecho
    #p/ q funcione en navegador, a la ruta de home añadir:
    #/v0/book_id
    # ?id=2 --> p/ añadir el arg del id deseado (2 p. ej.)


# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
@app.route('/v0/book/<string:title>', methods=["GET"])
def book_title(title):
    results=[title for title in books if book['title'].lower()==title]
    return results
    #check original; BUT esta es otra forma de hacerlo, en vez d con args, especificando q se va a meter str


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
# @app.route('/v1/book', methods=["GET"])
    
    #VER ORIG, hecho en postman tb

# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/v1/book_insert',methods=['POST'])
def book_insert():
    id=int(request.args['id'])
    title=request.args['title']
    author=request.args['author']
    first_sentence=request.args['first_sentence']
    published=int(request.args['published'])

    new_book={'id': id,
     'title': title,
     'author': author,
     'first_sentence': first_sencence,
     'published': published}
    books.append(new_book)
    return 'Libro guardado',books
    

# 6.Ruta para añadir un libro mediante parámetros
# P/ METERLO EN URL: http://127.0.0.1:5000/v1/book_insert?id=4&title=libro1&author=Pepe&first_sentence=x&published=20
@app.route('/v1/book_insert',methods=['POST'])
def book_insert():
    id=int(request.args['id'])
    title=request.args['title']
    author=request.args['author']
    first_sentence=request.args['first_sentence']
    published=int(request.args['published'])

    new_book={'id': id,
     'title': title,
     'author': author,
     'first_sentence': first_sentence,
     'published': published}
    books.append(new_book)

    return new_book 

# 7.Ruta para modificar un libro


# 8.Ruta para eliminar un libro


app.run()