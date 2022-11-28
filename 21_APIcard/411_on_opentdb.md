Collected Knowledge & Wisdom on
# OpenTriviaDatabase
---
## Provides:
Access to randomized trivia questions.

### Pain factor: _
(0=ezpz...5=nightmare)

### Key Provisioning:     
- No key needed to access this API

Sample code to access a random Computer Science question:

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
    print (data_json)
    return data_json

if __name__ == "__main__":
    app.debug = True
    app.run()

### Quotas:
- A Maximum of 50 Questions can be retrieved per call.
- Only 1 Category can be requested per API Call. To get questions from any category, don't specify a category.

---

## The Good:
- Allows access to thousands of trivia questions.
- CLearly states limitations in documentation.
- URLS are clear and easy to understand
## The Bad:
- 
## The Ugly:
- ...


**Location:** https://opentdb.com/ https://opentdb.com/api.php?amount=1&category=18

---

Accurate as of (last update):    2022-11-23

Contributors: Vivian Graeber, pd2  