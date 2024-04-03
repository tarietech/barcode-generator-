# barcode-generator-
Barcode Generator Manual
Overview

The Barcode Generator is a simple application that allows users to create various types of barcodes, including EAN-13, Code128, UPC-A, and QR codes. This manual provides instructions on how to operate the Barcode Generator application.
Installation

    Ensure you have Python installed on your system. You can download Python from the official website.
    Install the required libraries by running the following command in your terminal:

    pip install python-barcode qrcode

Usage

    Launch the Application:
        Open your terminal/command prompt.
        Navigate to the directory where the barcode_generator.py file is located.
        Run the following command:

        python barcode_generator.py

    Input Barcode Details:
        Once the application window opens, you will see fields for "Barcode Type," "Data," and "Save As."
        Enter the following details:
            Barcode Type: Choose the type of barcode you want to generate. Supported types include EAN-13, Code128, UPC-A, and QR Code.
            Data: Enter the data you want to encode into the barcode.
            Save As: Specify the filename and location where you want to save the generated barcode image.

    Generate Barcode:
        After entering the barcode details, click on the "Generate Barcode" button.
        If all fields are filled correctly and the barcode type is supported, the application will generate the barcode image and save it to the specified location.
        If any errors occur during the generation process, an error message will be displayed, indicating the nature of the error.

    Exit the Application:
        To exit the application, simply close the application window.

Supported Barcode Types

The Barcode Generator supports the following barcode types:

    EAN-13
    Code128
    UPC-A
    QR Code

Error Handling

    If any of the input fields are left blank, an error message will prompt you to fill in all fields.
    If an unsupported barcode type is entered, an error message will inform you that the barcode type is not supported.
