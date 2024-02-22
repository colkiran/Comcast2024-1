
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")         # home page
def home():
    return render_template("index01.html", adj = "This is my first web page development using FLASK", x = 500)

if __name__ == '__main__':
    app.run()
