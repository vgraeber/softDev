'''
VAT: Vivian Graeber, Ayman Habib, Talia Hsia
SoftDev
K07 -- Learning Flask
2022-10-03
time spent: 15 min
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?

'''
DISCO:

QCC:
0. java
1. location indicators
2. the terminal
3. it'll print __main__
4. the website; i saw it
5. java
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''