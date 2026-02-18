from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice', methods=['GET'])
def roll_dice():
    # From original dice.py - random.randint(1, 10)
    result = random.randint(1, 10)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
