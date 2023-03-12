# step1 importing the  module

from flask import Flask, request

# step2 creation of object with a parameter __name__

app = Flask(__name__)

# step3  create an endpoint using routes and bind them with a functionality
@app.route('/')
def home_page():
    return "Welcome..!"

@app.route('/about')
def about_page():
    return "Welcome to my portfolio website - https://bhaskarchakali.github.io/portfolio-website/"

@app.route('/square')
def Square_page():
    a = int(request.args.get('a'))
    return str(a**2)

@app.route('/upper')
def Upper_case():
    a = request.args.get('a')
    return a.upper()

@app.route('/factorial')
def factorial_page():
    a = int(request.args.get('a'))
    x = 1
    for i in range(a, 0, -1):
        x = x*i

    return str(x)

@app.route('/noofdigit')
def nod_page():
    a = int(request.args.get('a'))
    b = str(a)
    return str(len(b))

@app.route('/data')
def IRL():
    if 3*0.1 == 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS"
    elif 3*0.1 == 0.3 and 4*0.1 != 0.4:
        return "INNOMATICS RESEARCH"

    elif 3*0.1 != 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS RESEARCH LAB"



# step4 Run the flusk application
if __name__ == "__main__":
    app.run(debug=True)
