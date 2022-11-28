from urllib.request import urlopen
import json

from flask import Flask, render_template

app = Flask(__name__)    #create Flask object
#FUTURE PLANS MAKE SURE TO CHECK IF FORMS ARE VALID

api = "https://opentdb.com/api.php?amount=1&category=18"
@app.route("/")
def question():
    call = urlopen(api)
    data_json = json.loads(call.read())
    results_json = data_json["results"]
    difficulty = results_json[0]["difficulty"]
    question = results_json[0]["question"]
    correct = results_json[0]["correct_answer"]
    incorrect = results_json[0]["incorrect_answers"]
    print(difficulty)
    print(question)
    print(correct)
    print(incorrect)
    return render_template("main.html", url=url, explanation = explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()