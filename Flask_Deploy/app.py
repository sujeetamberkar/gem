import os
import string
import re
import PyPDF2
from flask import Flask, render_template, request
app = Flask(__name__)

def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def remove_non_ascii(a_str):
    ascii_chars = set(string.printable)
    return ''.join(filter(lambda x: x in ascii_chars, a_str))

def remove_multiple_newlines(input_string):
    output_string = re.sub(r'(\n\s*)+', '\n', input_string)
    return output_string

def extract_data(input_string):
    bid_end_date_time = re.search(r'Bid End Date/Time/\n/\n/\n(.*?)\n', input_string)
    department_name = re.search(r'Department Name/\n(.*?)\n', input_string)
    total_quantity = re.search(r'Total Quantity/\n(.*?)\n', input_string)
    emd_amount = re.search(r'EMD Amount/\n(.*?)\n', input_string)

    bid_end_date_time = bid_end_date_time.group(1).strip() if bid_end_date_time else None
    department_name = department_name.group(1).strip() if department_name else None
    total_quantity = total_quantity.group(1).strip() if total_quantity else None
    emd_amount = emd_amount.group(1).strip() if emd_amount else None

    return {
        "Bid End Date/Time": bid_end_date_time,
        "Department Name": department_name,
        "Total Quantity": total_quantity,
        "EMD Amount": emd_amount
    }

@app.route('/')
def helloworld():
    return 'Hi'

@app.route('/s', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return "No file uploaded"

        pdf_file = request.files['pdf_file']

        if pdf_file.filename == '':
            return "No selected file"

        if pdf_file:
            filename = pdf_file.filename
            pdf_file_path = os.path.join('uploads', filename)
            pdf_file.save(pdf_file_path)

            extracted_text = extract_text_from_pdf(pdf_file_path)
            data = remove_non_ascii(extracted_text)
            cleaned_data = remove_multiple_newlines(data)
            extracted_data_dict = extract_data(cleaned_data)

            return render_template('result.html', data=extracted_data_dict)
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
