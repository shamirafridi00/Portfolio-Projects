import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__) #Initialize the flask App
#model = pickle.load(open('regression.pkl', 'rb'))


# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = joblib.load(open("r2.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result',methods=['POST'])
def result():
    
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list) 
        r = np.round(result,decimals=2)
        #prediction = r  

        #return render_template("result.html", prediction = r)
        return render_template('result.html', prediction='Estimated Car Price is PKR {} lakhs.'.format(r))


if __name__ == "__main__":
    app.run(debug=True)