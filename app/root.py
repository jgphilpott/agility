from flask import Flask

app = Flask("Agility", template_folder="app", static_folder="app")

@app.route("/")
def home():

    return "Agility"

app.run(host="0.0.0.0", port=4444, debug=True)
