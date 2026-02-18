from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Questions from original Trivia game.py
questions = {
    "What keyword is used to define a function in Python?": "def",
    "What data type is returned by the expression 3 / 2 in Python 3?": "float",
    "Which symbol is used to write a comment in Python?": "#",
    "What built-in function is used to get the length of a list?": "len()",
    "What keyword is used to handle exceptions in Python?": "try",
    "What is the output of print(type([]))?": "<class 'list'>",
    "Which Python data type is immutable: list or tuple?": "tuple",
    "What keyword is used to import a module in Python?": "import"
}

@app.route('/')
def index():
    if 'current_questions' not in session:
        start_game()
    return render_template('index.html')

@app.route('/start_game', methods=['GET'])
def start_game():
    question_list = list(questions.keys())
    selected_questions = random.sample(question_list, min(5, len(question_list)))
    session['current_questions'] = selected_questions
    session['current_question_idx'] = 0
    session['score'] = 0
    return jsonify({'success': True})

@app.route('/get_question', methods=['GET'])
def get_question():
    if 'current_questions' not in session:
        start_game()
    
    idx = session.get('current_question_idx', 0)
    questions_list = session.get('current_questions', [])
    
    if idx >= len(questions_list):
        return jsonify({'game_over': True, 'score': session.get('score', 0), 'total': len(questions_list)})
    
    question = questions_list[idx]
    return jsonify({
        'question': question,
        'question_number': idx + 1,
        'total_questions': len(questions_list)
    })

@app.route('/answer/<answer>', methods=['POST'])
def answer(answer):
    idx = session.get('current_question_idx', 0)
    questions_list = session.get('current_questions', [])
    
    if idx >= len(questions_list):
        return jsonify({'error': 'Game over'})
    
    question = questions_list[idx]
    correct_answer = questions[question].lower().strip()
    user_answer = answer.lower().strip()
    
    is_correct = user_answer == correct_answer
    if is_correct:
        session['score'] = session.get('score', 0) + 1
    
    session['current_question_idx'] = idx + 1
    
    return jsonify({
        'correct': is_correct,
        'correct_answer': questions[question],
        'score': session.get('score', 0)
    })

if __name__ == '__main__':
    app.run(debug=True)
