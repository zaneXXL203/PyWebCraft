from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

FILE_NAME = 'to-do list.json'

def load_tasks():
    """Load tasks from JSON - from original to-do list.py"""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        except:
            return {'tasks': []}
    return {'tasks': []}

def save_tasks(data):
    """Save tasks to JSON - from original to-do list.py"""
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(data, f)
    except:
        print('Failed to Save.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks['tasks'])

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    description = data.get('description', '').strip()
    
    if not description:
        return jsonify({'error': 'Task description cannot be empty'})
    
    tasks_data = load_tasks()
    tasks_data['tasks'].append({'description': description, 'complete': False})
    save_tasks(tasks_data)
    
    return jsonify({'success': True})

@app.route('/complete_task/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    tasks_data = load_tasks()
    if 0 <= task_id < len(tasks_data['tasks']):
        tasks_data['tasks'][task_id]['complete'] = True
        save_tasks(tasks_data)
        return jsonify({'success': True})
    return jsonify({'error': 'Task not found'})

@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks_data = load_tasks()
    if 0 <= task_id < len(tasks_data['tasks']):
        del tasks_data['tasks'][task_id]
        save_tasks(tasks_data)
        return jsonify({'success': True})
    return jsonify({'error': 'Task not found'})

if __name__ == '__main__':
    app.run(debug=True)
