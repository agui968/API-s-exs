import pandas as pd
import os
import pickle
from flask import Flask, jsonify, request
os.chdir(os.path.dirname(__file__))


data=pd.read_csv('data/')

#IMPORT THE TRAINED MODEL
with open('..\\models\\final_model_gbc.pkl', 'rb') as input:
    model = pickle.load(input) 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>My API</h1><p>This site is a prototype API for distant reading of XXX.</p>"
