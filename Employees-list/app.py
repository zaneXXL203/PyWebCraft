from flask import Flask, render_template, request, jsonify, send_file
import csv
import io

app = Flask(__name__)

# Original data from Employees.py
employees = [["name", "age", "job"],
             ["spongebob", 46, "Fry Cook"],
             ["Patrick", 40, "Jobless"],
             ["Sandy", 29, "Scientist"]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_employees', methods=['GET'])
def get_employees():
    return jsonify({'employees': employees[1:]})

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    name = data.get('name', '').strip()
    age = data.get('age', '')
    job = data.get('job', '').strip()
    
    if not name or not age or not job:
        return jsonify({'error': 'All fields are required'})
    
    try:
        age = int(age)
        employees.append([name, age, job])
        return jsonify({'success': True})
    except ValueError:
        return jsonify({'error': 'Age must be a number'})

@app.route('/export_csv', methods=['GET'])
def export_csv():
    # Logic from original Employees.py
    output = io.StringIO()
    writer = csv.writer(output)
    for row in employees:
        writer.writerow(row)
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name='employees.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
