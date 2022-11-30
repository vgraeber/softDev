Collected Knowledge & Wisdom on
# OpenTriviaDatabase

---

## Provides:
Access to randomized trivia questions.

### Pain factor: _
0 - Has an API generator that allows you to get an API link in moments, with all of your specified requirements

### Key Provisioning:     
- No key needed to access this API

---

Sample code to access a random Computer Science question:

from urllib.request import urlopen
import json

api = "https://opentdb.com/api.php?amount=1&category=18"

def test():
    call = urlopen(api)
    data_json = json.loads(call.read())
    print (data_json)
    return data_json

test()

---

### Quotas:
- A Maximum of 50 Questions can be retrieved per call.
- Only 1 Category can be requested per API Call. To get questions from any category, don't specify a category.

---

## The Good:
- Has an API generator, so you don't have to do any heavy lifting
- Allows access to thousands of trivia questions
- CLearly states limitations in documentation
- URLS are clear and easy to understand
## The Bad:
- N/A
## The Ugly:
- N/A


**Location:** https://opentdb.com/api_config.php

---

Accurate as of (last update):    2022-11-29

Contributors: Vivian Graeber, pd2  