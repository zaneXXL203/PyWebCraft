from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Logic from original guess the number.py
def check_guess(user_number, random_number):
    if user_number == random_number:
        return 'correct'
    elif user_number > random_number:
        return 'high'
    else:
        return 'low'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    try:
        user_guess = int(data.get('guess'))
        secret_number = session.get('number')
        session['attempts'] = session.get('attempts', 0) + 1
        
        result = check_guess(user_guess, secret_number)
        
        if result == 'correct':
            message = f'🎉 Congratulations! You guessed the correct number {secret_number} in {session["attempts"]} attempts!'
            session.clear()
        elif result == 'high':
            message = f'{user_guess} TOO HIGH!'
        else:
            message = f'{user_guess} TOO LOW!'
        
        return jsonify({'result': result, 'message': message})
    except ValueError:
        return jsonify({'error': 'Please enter a valid number'})

@app.route('/reset', methods=['GET'])
def reset():
    session.clear()
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
