# PDF Data Extractor README
This repository contains a Python script (code.py) that extracts specific information from a PDF file, such as Bid End Date/Time, Department Name, Total Quantity, and EMD Amount. The program reads a PDF file, strips out non-ASCII characters, removes excessive newlines, and uses regex to extract the desired data.
## Prerequisites
    Python 3.6 or above
    Python pip (Python package installer)

## Installation
  1) Download and install Python from [here](https://www.python.org/downloads/)
     Make sure to select the checkbox that says "Add Python 3.x to PATH" during installation to ensure the Python and pip are added to your environment variables. This allows you to run Python and pip from your command prompt.
     
  2) Clone this repository into your local machine.
     git clone <repository_url>

  3) Change directory to the cloned repository.
     cd <repository_directory>
  4) Install the necessary Python libraries using pip.
     pip install -r requirements.txt
## Running the Script
  1) Ensure your PDF file is in the same directory as the code.py file.
  2) Run the Python script using the command
     python code.py
  3) When prompted, enter the name of your PDF file, including its file extension (e.g., example.pdf).
  4) The script will extract the required information from the PDF and print it in the console. If the script cannot find the PDF file or encounters an error during execution, it will print an appropriate error message.
Note: This script continuously asks for a valid PDF file name until it successfully extracts the data or encounters an unknown error

## Python Libraries Used
  1) PyPDF2 for reading and extracting text from PDF files.
  2) string and re (regular expressions) for text cleaning and data extraction

### Author
Sujeet Amberkar
