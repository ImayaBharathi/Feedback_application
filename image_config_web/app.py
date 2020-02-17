from flask import Flask,render_template,request,jsonify
from store_feedback import submit_feedback
import pymysql


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    response = submit_feedback(request.form["rating"],request.form["comment"],request.form["file_name"])
    return render_template("dashboard.html",data=response["values"])

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")