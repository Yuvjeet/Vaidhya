import pickle
import pandas as pd
import numpy as np
import joblib

symptoms = ['itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'excessive hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze']

with open('svm_model.pkl', 'rb') as f:
    svm = pickle.load(f)
with open('nb_model.pkl', 'rb') as f:
    nb = pickle.load(f)
# dt = joblib.load('decision_tree.joblib')
# mnb = joblib.load('mnb.joblib')
# rf = joblib.load('random_forest.joblib')
# gb = joblib.load('gradient_boost.joblib')
def svm_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = svm.predict(symptom)
    return pred

def nb_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = nb.predict(symptom)
    return pred
def dt_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = dt.predict(symptom)
    return pred
def mnb_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = mnb.predict(symptom)
    return pred
def rf_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = rf.predict(symptom)
    return pred
def gb_model(l):
    symptom = np.zeros(132, dtype=int).reshape(1,-1)
    for i in l: symptom[0][symptoms.index(i)] = 1
    pred = gb.predict(symptom)
    return pred

print(len(symptoms))