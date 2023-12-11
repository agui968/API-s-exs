from flask import Flask, request, jsonify
import os
import pickle
# from sklearn.model_selection import cross_val_score
import pandas as pd

import sqlite3


os.chdir(os.path.dirname(__file__))

# sqlite3 advert.db #on terminal
datacsv=pd.read_csv('data/Advertising.csv')

newdb=advert.db
db=Advertising
connection = sqlite3.connect(newdb)
cursor = connection.cursor()
cursor.execute(f"CREATE TABLE IF NOT EXISTS {Advertising} (TV INTEGER, radio REAL, newpaper REAL, sales REAL);")

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido a mi API del modelo advertising"

# 1. Endpoint que devuelva la predicción de los nuevos datos enviados mediante argumentos en la llamada
@app.route('/v1/predict', methods=['GET'])
def predict():
    model = pickle.load(open('data/advertising_model','rb'))

    tv = request.args.get('TV', None)
    radio = request.args.get('radio', None)
    newspaper = request.args.get('newspaper', None)

    if tv is None or radio is None or newspaper is None:
        return "Missing args, the input values are needed to predict"
    else:
        prediction = model.predict([[int(tv),int(radio),int(newspaper)]])
        return "The prediction of sales investing that amount of money in TV, radio and newspaper is: " + str(round(prediction[0],2)) + 'k €'


#insert into
query = "INSERT INTO advertising (TV, radio, newpaper, sales) VALUES (?, ?, ?,?)"
cursor.execute(data['TV'], data['radio'], data['newpaper'], data['sales'])







#2
def ingest_data():
    # con = sqlite3.connect(os.path.join('data', 'db.db'))
    data = request.json
    query = "INSERT INTO advertising (TV, radio, newpaper, sales) VALUES (?, ?, ?,?)"
    connection.execute(query, (data['TV'], data['radio'], data['newpaper'], data['sales']))
    connection.commit()
    connection.close()
    return jsonify({'message': 'Data updated'})

app.run()