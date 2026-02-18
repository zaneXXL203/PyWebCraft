from flask import Flask, render_template, request, jsonify
import datetime
import time
import threading

app = Flask(__name__)

alarm_thread = None
alarm_running = False

# Logic from original AlarmClock.py
def set_alarm(alarm_time):
    global alarm_thread, alarm_running
    
    try:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
    except:
        return False
    
    def check_and_alarm():
        global alarm_running
        alarm_running = True
        
        while alarm_running:
            current_time = datetime.datetime.now().strftime("%H:%M")
            
            if current_time == f"{alarm_hour:02d}:{alarm_minute:02d}":
                alarm_running = False
                return True
            
            time.sleep(1)
    
    alarm_thread = threading.Thread(target=check_and_alarm, daemon=True)
    alarm_thread.start()
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_alarm', methods=['POST'])
def set_alarm_route():
    global alarm_running
    
    data = request.json
    alarm_time = data.get('time')
    
    if not alarm_time:
        return jsonify({'error': 'Please enter a time'})
    
    try:
        set_alarm(alarm_time)
        return jsonify({'success': True, 'message': f'Alarm set for {alarm_time}'})
    except ValueError:
        return jsonify({'error': 'Invalid time format. Use HH:MM'})

@app.route('/stop_alarm', methods=['GET'])
def stop_alarm():
    global alarm_running
    alarm_running = False
    return jsonify({'success': True, 'message': 'Alarm stopped'})

if __name__ == '__main__':
    app.run(debug=True)
