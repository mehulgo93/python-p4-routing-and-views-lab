#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
        return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
        print(param)
        return param


@app.route('/count/<int:param>')
def count(param):
        numbers = '\n'.join(str(i) for i in range(0, param + 1))
        return numbers


@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
        print(num1, operation, num2)
        result = None
        if operation == "+":
            result = num1 + num2
        elif  operation == "-":
            result = num1 - num2
        elif operation == "*":
              result = num1 * num2
        elif operation == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero"
        elif operation == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                return "Error: Modulo by zero"
        else:
            return "Invalid operation"
        
        return str(result)




