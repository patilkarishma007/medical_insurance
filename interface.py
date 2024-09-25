from flask import Flask,render_template,request,jsonify
from utils import MedicalInsurance , load_dataset
from flask_cors import CORS
import config
med_ins=MedicalInsurance()
df=load_dataset()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/smoker_options')  # Change to plural "smoker_options"
def smoker_options():
    df['smoker'] = df['smoker'].apply(lambda x: x.lower())
    return jsonify(list(df['smoker'].unique()))

@app.route('/gender_options')  # Change to plural "gender_options"
def gender_options():
    df['gender'] = df['gender'].apply(lambda x: x.lower())
    return jsonify(list(df['gender'].unique()))


@app.route('/region_options')
def region_options():
    return jsonify(list(df['region'].unique()))


@app.route('/prediction',methods=['POST'])
def prediction():
    data = request.form
    print(data)

    age=data['age']
    gender= data['gender']
    bmi=data['bmi']
    children = data['children']
    smoker=data['smoker']
    region=data['region']

    med_ins=MedicalInsurance()
    pred_charges=med_ins.get_predicated_charges(age,gender,bmi,children,smoker,region)
    print(f"Predicted charges: {pred_charges}")
    return jsonify({'predicted Medical Insurance Charges': pred_charges})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.FLASK_PORT_NUMBER,debug=True)