import pickle
from flask import Flask , request, app ,jsonify, url_for, render_template
import numpy as np 
import pandas as pd 

app= Flask(__name__)

regmodel=pickle.load(open('regmodel.pkl','rb'))
scaler=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    return jsonify(output[0])

@app.route('/predict',methods=["POST"])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template('home.html',predection_text=f"The house price is {output}")
if __name__=="__main__":
    app.run(debug=True)