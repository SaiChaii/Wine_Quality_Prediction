import numpy as np
from flask import Flask, request, render_template
import joblib


app = Flask(__name__)
#model = joblib.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

def predict_quality(input_values):
    # Your IPython notebook code for wine quality prediction with the 11 variables
    # ...

    # For example, a dummy implementation that returns a static prediction:
    model = joblib.load(open('model_1.0.2.pkl', 'rb'))
    prediction = model.predict(input_values)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    if request.method == 'POST':
        text1 =float( request.form['Enter Fixed Acidity'] )
        text2 =float( request.form['Enter Volatile Acidity'])
        text3 =float( request.form['Enter Citric Acidity'])
        text4 =float( request.form['Enter Residual Sugar Content'])
        text5 =float( request.form['Enter Free Chlorides'])
        text6 =float( request.form['Enter Free Sulphur Dioxide'])
        text7 =float( request.form['Enter Total Sulphur Dioxide'])
        text8 =float( request.form['Enter Density'])
        text9 =float( request.form['Enter pH'])
        text10 =float( request.form['Enter Sulphates'])
        text11 =float( request.form['Enter Alcohol'])
        calls=[text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11]
    


    calls=np.array(calls)
    data = [calls]
    c=calls.reshape(1,-1)
    prediction=predict_quality(calls)
    
    if prediction[0]:
        return render_template('index.html', prediction_text='The Mammogram is malignant')
    else:
        return render_template('index.html', prediction_text='The Mammogram is benign')
    
if __name__ == "__main__":
    app.run(debug=True)