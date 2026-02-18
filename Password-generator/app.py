from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Logic from original passwordgenerator.py
def password_generator(length, uppercase=False, special=False, digits=False):
    if length < 4:
        raise ValueError('Character needs to be at least 4 characters')
    
    lower = string.ascii_lowercase
    uppercase_str = string.ascii_uppercase if uppercase else ""
    special_str = string.punctuation if special else ""
    digit_str = string.digits if digits else ""
    
    all_chars = lower + uppercase_str + special_str + digit_str
    
    required_characters = []
    if uppercase:
        required_characters.append(random.choice(uppercase_str))
    if special:
        required_characters.append(random.choice(special_str))
    if digits:
        required_characters.append(random.choice(digit_str))
    
    remaining_length = length - len(required_characters)
    password = required_characters
    
    for _ in range(remaining_length):
        characters = random.choice(all_chars)
        password.append(characters)
    
    random.shuffle(password)
    return "".join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    try:
        length = int(data.get('length', 12))
        uppercase = data.get('uppercase', False)
        special = data.get('special', False)
        digits = data.get('digits', False)
        
        password = password_generator(length, uppercase, special, digits)
        return jsonify({'password': password})
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
