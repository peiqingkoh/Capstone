from flask import Flask, jsonify, request, render_template
import joblib
import sklearn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

import nltk

from bs4 import BeautifulSoup  
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import regex as re

app = Flask(__name__)

stopwords = stopwords.words('english')
newStopWords = ['southwestair','delta','airasiasupport','americanair','british']
stopwords.extend(newStopWords)
stops = set(stopwords)
      
@app.route('/predict-airline',methods=['GET','POST'])
def predict_airline():

    airline = joblib.load(r"C:\Users\PQKoh\virtualenvs\flaskservice\my_model_lr.pkl")
    cvec = joblib.load(r"C:\Users\PQKoh\virtualenvs\flaskservice\my_cvec.pkl")

    output = None

    if request.method == "POST": 

        msg = request.form["msg"]
        corpus = []

        BS = BeautifulSoup(msg)
        msg_BS = BS.get_text()

        letters_only = re.sub("[^a-zA-Z]", " ", msg_BS)
        letters_only = letters_only.lower()

        tokenizer = RegexpTokenizer('[a-zA-z]\w+')
        combine_tokens = tokenizer.tokenize(letters_only)
 
        stops = set(stopwords)

        remove_stop_words = [w for w in combine_tokens if not w in stops]

        lemmatizer = WordNetLemmatizer()
        meaningful_words = [lemmatizer.lemmatize(i) for i in remove_stop_words]
    
        meaningful_words = " ".join(meaningful_words)
        corpus.append(meaningful_words)
  
        unseen_msg = cvec.transform(corpus)
        output = airline.predict(unseen_msg)
        if output == 0:
            output = 'AirAsiaSupport'
        elif (output == 1):
            output = 'AmericanAir'
        elif (output == 2):
            output = 'British_Airways'
        elif (output == 3):
            output = 'Delta'
        else:
            output = 'SouthwestAir'
    return render_template("base.html", output = output)

@app.route('/')
def hello_world():
    return 'Welcome to DSI 10 :)'



