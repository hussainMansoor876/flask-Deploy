from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():
    file = request.files['file']
    try:
        data = pd.read_csv(file, header=None)
        totalTime = ((data[0][0] * 10) + data[1][0]) + ((len(data[0][data[0] == 0]) - 1)
                                                        * 1024 * 10) + ((data[0].iloc[-1] * 10) + data[1].iloc[-1])
        removeDup = data[1].unique()
        legend = 'Result'
        data1 = data.groupby([0, 1]).sum()
        x = data1.reset_index()
        labels = ["January", "February", "March",
                "April", "May", "June", "July", "August"]
        values = [10, 9, 8, 7, 6, 4, 7, 8]
        return render_template('result.html', totalTime=totalTime, removeDup=removeDup,  values=x[5], labels=x[1], legend=legend)
    except:
        data = pd.read_excel(file, header=None)
        totalTime = ((data[0][0] * 10) + data[1][0]) + ( (len(data[0][data[0] == 0]) - 1) * 1024 * 10) + ((data[0].iloc[-1] * 10) + data[1].iloc[-1])
        removeDup = data[1].unique()
        legend = 'Result'
        data1 = data.groupby([0, 1]).sum()
        x = data1.reset_index()
        labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
        values = [10, 9, 8, 7, 6, 4, 7, 8]
        return render_template('result.html', totalTime=totalTime, removeDup=removeDup,  values=x[5], labels=x[1], legend=legend)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
