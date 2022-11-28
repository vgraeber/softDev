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
    type = results_json[0]["type"]
    question = results_json[0]["question"]
    correct = results_json[0]["correct_answer"]
    incorrect = results_json[0]["incorrect_answers"]
    print(difficulty)
    print(type)
    print(question)
    print(correct)
    print(incorrect)
    #sorting all of the answers
    if (type == "boolean"):
        all_answers = ['True', 'False']
        all_answers.sort(reverse=True)
    elif (type == "multiple"):
        all_answers = incorrect.copy()
        all_answers.append(correct)
        all_answers.sort()
    #making the 2 types of quotes print correctly
    question = question.replace("&quot;", '"')
    question = question.replace("&#039;", "'")
    for i in range(len(all_answers)):
        all_answers[i] = all_answers[i].replace("&quot;", '"')
        all_answers[i] = all_answers[i].replace("&#039;", "'")
    return render_template("main.html", question = question, answers = all_answers)

if __name__ == "__main__":
    app.debug = True
    app.run()