from mgmbanking import app
from flask import render_template


# Home Route

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/contact")
def creditcard():
    return render_template("contact.html")
