from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

car_started = False

# Logic from original simple car helper.py
def process_command(command):
    global car_started
    command = command.lower().strip()
    
    if command == 'start':
        if car_started:
            return 'error', 'CAR is already started'
        car_started = True
        return 'success', 'STARTING the car...'
    elif command == 'stop':
        if car_started:
            car_started = False
            return 'success', 'STOPPED the car...'
        else:
            return 'error', 'CAR is already STOPPED'
    elif command == 'help':
        return 'info', 'START - start the car. | STOP - stop the car. | QUIT - end the program.'
    else:
        return 'error', "I don't understand"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute_command', methods=['POST'])
def execute_command():
    data = request.json
    command = data.get('command', '')
    
    status, message = process_command(command)
    return jsonify({'status': status, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)
