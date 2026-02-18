# QR Code Generator

## Description
A simple tool that generates QR codes from text or URLs. Users can input data and specify a filename, and the tool creates a QR code image file.

## Features
- Generate QR codes from text or URLs
- Customizable box size (10 pixels)
- Customizable border width (4 pixels)
- Black and white color scheme
- Save QR codes as image files
- Simple command-line interface

## Usage
1. Run the script: python QRCODE_generator.py
2. Enter a text or URL when prompted
3. Enter the desired filename for the QR code image
4. The QR code image will be saved with the specified filename

## Example
Enter a TEXT or URL: https://www.example.com
Enter file name: qrcode.png
QR CODE saved as! QRCODE.PNG

## Requirements
- Python 3.x
- qrcode library (pip install qrcode[pil])
- Pillow library (pip install Pillow)
