from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(f"Printed in the console: {param}")
    return f'<h2>Printed in the browser: {param}</h2>'

@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return f'<h2>{num1} {operation} {num2} = {result}</h2>'

if __name__ == '__main__':
    app.run(debug=True)
