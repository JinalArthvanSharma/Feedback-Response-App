# Feedback Form Flask App

The website is made responsive using Bootstrap and includes some additional JavaScript functionalities.

## Screenshots 
- Home Page
![HomePage](/screenshot1.png)

- Feedback Form Page
![Feedback](/screenshot2.png)

- Thank you Page
![Feedback](/screenshot3.png)

## Installation

To run the Feedback Form Flask App locally, follow these steps:

1. Create a virtual environment for the project.

```
pip install virtualenv
virtualenv venv
```

2. Install the required dependencies using the following command:
```
pip install -r requirements.txt
```

3. Set up the `.env` file located in the `feedback` folder and add the following variables:

```
AZURE_ENDPOINT_URI=<YOUR_AZURE_ENDPOINT>
AZURE_KEY=<YOUR_AZURE_COG_SERVICE_APIKEY>
OPENAI_APIKEY=<YOUR_OPENAI_APIKEY>
SECRETKEY=<YOUR_FLASK_SECRETKEY>
```

## Usage

To run the app, use the following command:

```
python3 run.py
```

Access the app in your browser at `http://localhost:5000`.
[Demo app] https://feedbackexample.pythonanywhere.com/
