from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/learnmore", methods=["GET"])
def learn_more():
    return render_template("learnmore.html")

if __name__ == '__main__':
    home()
