from flask import Flask, make_response, send_file
import json

app = Flask(__name__)


@app.route("/patientpdf/<patientID>", methods=["GET"])
def get_pdf(patientID=None):
    if patientID is not None:
        path = f"data/patients/{patientID}.pdf"
        return send_file(path, as_attachment=False)

@app.route("/userdata", methods=["GET"])
def get_user_data():
    with open("data/patients/patients.json", "r") as f:
        data = json.load(f)
        return data

@app.route("/createaccount", methods=["POST"])
def create_account():
    pass

if __name__ == '__main__':
    app.run()