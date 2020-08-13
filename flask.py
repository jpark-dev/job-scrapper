from flask import Flask

app = Flask("scrapper!!!")

@app.route("/")
def home():
    return "hello!"