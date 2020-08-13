from flask import Flask, render_template, request, redirect
from sof import get_jobs

app = Flask("scrapper!!!")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect("/")
    return render_template("report.html", searchWord=word)