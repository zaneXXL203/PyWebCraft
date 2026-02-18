from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# From original rock paper and scissors.py
emojis = {
    "R": "🪨",
    "P": "📃",
    "S": "✂️",
}

def play_game(user_choice):
    computer_choice = random.choice(list(emojis.keys()))
    
    if user_choice == computer_choice:
        result = 'TIE'
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'S' and computer_choice == 'P') or \
         (user_choice == 'P' and computer_choice == 'R'):
        result = 'WIN'
    else:
        result = 'LOSE'
    
    return result, computer_choice

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<choice>', methods=['GET'])
def play(choice):
    choice = choice.upper()
    
    if choice not in emojis:
        return jsonify({'error': 'Invalid choice'})
    
    result, computer_choice = play_game(choice)
    
    return jsonify({
        'user_choice': emojis[choice],
        'computer_choice': emojis[computer_choice],
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
