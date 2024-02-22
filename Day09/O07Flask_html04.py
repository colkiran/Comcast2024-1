
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World <h1>"
@app.route("/<name>")
def user(name):
    return render_template("index03.html", usname=name, content="Friuits available in all Seasons", fruits = ['Apple', 'Orange', 'Pineapple', 'Gauva', 'Banana', "Watermelon"])

if __name__ == '__main__':
    app.run(debug=True)

