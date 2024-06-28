from flask import Flask, render_template

app = Flask(import_name = "Flask Practice")

@app.route("/")

def home_page():
    return render_template("home1.html")

if __name__ == "__main__":
    app.run(debug = True)