from flask import Flask
from flask import render_template, request 
#backend Programming, now not using anymore, have to be front end#
app= Flask(__name__)
#sign,if anything wrong render will look for you#
@app.route("/", methods=["GET","POST"])
#the action, POST, from backend to frontend . GET, frontend to backend#
def index():
    return (render_template("index.html"))

@app.route("/prediction_DBS", methods=["GET","POST"])

def prediction_DBS():
    return (render_template("index.html"))
if __name__ == "__main__":
    app.run()
