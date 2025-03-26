#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route(f'/print/<string:parameter>')
def print_text(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count_route(number):
    return "\n".join(str(i) for i in range(0, number))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    nnum1=int(num1)
    nnum2=int(num2)
    if operation=='+':
        result = nnum1 + nnum2
    elif operation =='-':
        result = nnum1 - nnum2
    elif operation =='*':
        result = nnum1 * nnum2
    elif operation =='div':
        result = nnum1 / nnum2
    elif operation =='%':
        result = nnum1 % nnum2
    return str(result)
    
