from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/") #these functions can now be accessed by both routes
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)
