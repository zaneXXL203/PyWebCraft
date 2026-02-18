# Excel Automation

## Description
An automated Excel processing tool that applies a 10% discount to product prices and generates a bar chart visualization of the discounted prices.

## Features
- Load Excel workbooks dynamically
- Apply 10% discount to price column
- Store corrected prices in a new column
- Automatically generate bar charts
- Save modified workbook with visualizations

## How It Works
1. Reads data from an Excel file (Sheet1)
2. Calculates 10% discount on prices in column 3
3. Stores corrected prices in column 4
4. Creates a bar chart visualization
5. Saves the updated workbook

## Usage
1. Prepare an Excel file with price data in column 3
2. Run the script: python EXCEL.py
3. Provide the filename to process
4. The modified file will be saved with charts added

## Requirements
- Python 3.x
- openpyxl library (pip install openpyxl)
