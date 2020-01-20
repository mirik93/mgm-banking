from mgmbanking import app
from flask import render_template


# Home Route

@app.route("/home")
def home():
<<<<<<< HEAD
    return render_template("index.html")
=======
    return render_template("home.html")
>>>>>>> db801e459c57eeaff388cf4aa85316f441e6b8c8


@app.route("/contact")
def creditcard():
    return render_template("contact.html")
