
from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index04.html", uname= "Mohamed Ali")

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Success")
    resp.set_cookie("Cookie01", "Bangalore")
    resp.set_cookie("Cookie02", "Chennai")
    return resp

@app.route("/get_cookie")
def get_cookie():
    val1 = request.cookies.get("Cookie01")
    val2 = request.cookies.get("Cookie02")
    if val1 == None:
        val1 = "Cookie01 Deleted......"
    if val2 == None:
        val2 = "Cookie02 Deleted......."
    return f"<h2> First Cookie : {val1}  <br> Second Cookie : {val2} </h2>"

@app.route("/del_cookie")
def del_cookie():
    resp = make_response("Deleted cookie successfully.....")
    resp.delete_cookie("Cookie01")
    resp.delete_cookie("Cookie02")
    return resp

if __name__ == '__main__':
    app.run(debug=True)
