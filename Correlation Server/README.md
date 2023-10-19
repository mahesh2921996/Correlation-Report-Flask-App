# Correlation Report Application

## Overview
This is a **Python-based** application that allows users to find different types of _correlation pairs_. The application provides a **web interface** for users to find different _correlation pairs_.

## Introduction
In **data science**, correlation is an important concept to understand the _relationship_ between _numerical variables_. With the help of **Correlation Report Application**, we can easily tell how much two numerical variables are associated with each other. Generally, correlation can be classified into strong, moderate, weak etc. We get the _correlation matrix_ with the help of the _corr()_ function in **Pandas DataFrame**, but we can not easily get pairs of different types of correlation, e.g. Pairs of strong correlation variables. So, that **purpose**, we can make the app, which are _returns_ the different type of _correlation pairs_.

## Features
- User-Interface based application.
- Support for various correlation types pairs such as strong, weak, moderate, and more.
- Allow users to explore correlation pairs at any ranges in custom option.

## Environment Setup
- Python 3.x
- Flask web framework
- correlation_report library (user-defined library)
- Other dependencies (specified in requirements.txt)

## Installation
1. Clone this repository to your local machine.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows).
4. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Start the application: `python correlation_report_server.py`.
2. Hit the url on **`https://127.0.0.1:443/`**

## How to Use
- Upload a CSV or Excel file to start.
- Click the ``Correlation Types`` button to select different pairs, e.g. Strong Correlation Pairs, etc. 
- Once you click the ``Correlation Types`` button, choose the correlation pairs you wish to view.
- The ``Help`` button will provide guidance on how the correlation pairs' assigned ranges are.

## Deployment
- Deploy the application to a production server using a web server like Nginx or Apache, wsgi.
- Configure a production-ready web server to serve the Flask application.

## Contributing
Contributions are welcome! Please create a pull request or open an issue for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
