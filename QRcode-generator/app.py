from flask import Flask, render_template, request, jsonify
import qrcode
from datetime import datetime

app = Flask(__name__)

# Logic from original QRCODE_generator.py
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(filename)
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'Please enter text or URL'})
    
    try:
        filename = input("Enter file name: ").strip().upper() if False else f'qrcode_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        generate_qr_code(text, filename)
        return jsonify({'success': True, 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
