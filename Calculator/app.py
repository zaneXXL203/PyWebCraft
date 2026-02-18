from flask import Flask, render_template, request, jsonify
import sys
import os

app = Flask(__name__)

def calculate_result(num1, num2, operator):
    """Uses logic from original calculator.py"""
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError('Cannot divide by zero')
        result = num1 / num2
    else:
        raise ValueError('Invalid operator')
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        num1 = int(float(data.get('num1')))
        num2 = int(float(data.get('num2')))
        operator = data.get('operator')
        
        result = calculate_result(num1, num2, operator)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
