from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Logic from original message.py
def create_and_save_message(filename, message):
    if not filename:
        filename = 'default.txt'
    
    # Create the file
    with open(filename, 'w') as f:
        pass
    
    # Add the message
    if filename and message:
        with open(filename, 'a') as f:
            f.write(message)
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_message', methods=['POST'])
def create_message():
    data = request.json
    filename = data.get('filename', 'default.txt').strip()
    message = data.get('message', '').strip()
    
    if not filename:
        filename = 'default.txt'
    
    try:
        create_and_save_message(filename, message)
        return jsonify({'success': True, 'message': f'Message added to {filename}!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
