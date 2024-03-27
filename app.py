from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
import json
from pred import svm_model, dt_model, nb_model, mnb_model, rf_model, gb_model
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "BUILT TO TAKE CARE", black = True)
@app.route("/contact")
def contact():
    return render_template("contact.html", title = "CONTACT US", black = True)


@app.route('/test', methods=['POST'])
def test():
    try:
        data = request.get_json()
        symptoms = data['symptoms']
    except:
        return "Invalid payload", 400
    else:
        if symptoms == []: return "'Normal'"
        svm_pred = svm_model(symptoms)
        # dt_pred = dt_model(symptoms)
        nb_pred = nb_model(symptoms)
        # mnb_pred = mnb_model(symptoms)
        # rf_pred = rf_model(symptoms)
        seen, results = set(), ""
        seen.add(str(svm_pred))
        # seen.add(str(dt_pred))
        seen.add(str(nb_pred))
        # seen.add(str(mnb_pred))
        # seen.add(str(rf_pred))
        for i in seen:
            results += i + " "
        # gb_pred = gb_model(symptoms)
       # print("\n\nprediction : ", svm_pred)
        # print("\n\nprediction: ", dt_pred)
      #  print("prediction: ", nb_pred)
        # print("prediction: ", mnb_pred)
        # print("prediction: ", rf_pred)
        # print(data, "\n\n")
        return str(results)
# if __name__ == '__main__':
#     app.run(debug = True)
