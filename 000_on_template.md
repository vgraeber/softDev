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

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import urllib.request
import requests #https request module
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

API_URL = "https://opentdb.com/api.php?amount=1&category=18"
print("***DIAG: API key appended to https ***")
print(API_URL)

r = requests.get(API_URL) #creating a response object that will get us the information we need
# print("***DIAG: the contents of .content command ***")
# print(r.content) # shows the content of what the request got from the URL
# print("***DIAG: the contents of .json command ***")
# print(r.json()) #json decoder
api_dict = r.json() #r.json() returns a dictonary after deconding the response object
image_link = api_dict['hdurl'] #gets image from dictionary
explanation = api_dict['explanation'] #gets explaination from dictionary
title = api_dict['title']

@app.route("/" , methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'main.html', image=image_link, explanation=explanation, alt_text=title)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
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