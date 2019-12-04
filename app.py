from flask import Flask, render_template, request, jsonify
import pandas as pd
import random

data = pd.read_excel('data.xlsx', usecols='B,C,D,E,F,G') # Read data from excel
dict1 = {}

app = Flask(__name__)


@app.route('/') #Return the form
def index():
    for i in data:
        ind = random.randint(0, int(len(data[i].dropna())-1)) #generate the random number between 0 and len of column
        dict1[i] = data[i][ind] #assign the key and value base on random value
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    req = dict(request.form)
    return render_template('result.html', req=req, dict1=dict1, keys=data.columns)


if __name__ == "__main__":
    app.run(debug=True)
