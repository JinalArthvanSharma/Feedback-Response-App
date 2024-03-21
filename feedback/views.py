from flask import Blueprint, flash, redirect, render_template, request, url_for, send_file
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

home = Blueprint("homepage", __name__, url_prefix="/", static_folder="/static")

# Replace 'your_azure_key' with your actual Azure Text Analytics API key
azure_key = os.environ.get("AZURE_KEY")
endpoint = os.environ.get("AZURE_ENDPOINT_URI")

# Configure OpenAI API
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Azure Text Analytics client
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(azure_key))

@home.route("/")
@home.route("/index")
def homepage():
    return render_template("home.html")

@home.route("/feedback", methods=["GET", "POST"])
def feedbackpage():
    if request.method == "POST":
        name = request.form.get("nametxt");
        feedback = request.form.get("suggestbox")
        print(feedback)
        # Perform sentiment analysis using Azure Text Analytics API
        response = text_analytics_client.analyze_sentiment([feedback])
        # Extract sentiment score (positive, negative, neutral)
        print(response) 
        sentiment_score = response[0].sentiment
        print(sentiment_score)
        
        if sentiment_score == 'positive':
            prompt = "You received positive feedback on our product. Please respond with a brief acknowledgment and express gratitude for the feedback."
        elif sentiment_score == 'negative':
            prompt = "A user provided negative feedback about our product. Please respond empathetically, acknowledge the concerns raised, and assure them that we will address their issues promptly."
        else:
            prompt = "A user submitted neutral feedback. Please respond with a brief acknowledgment and thank them for taking the time to provide feedback."

        # Generate response using OpenAI
        generated_response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt} Feedback: {feedback}",
                }
            ],
            model="gpt-3.5-turbo",
        ).choices[0].message.content
        print(generated_response)
        return render_template("/thankyou.html", name=name, feedback=feedback, sentiment=sentiment_score, response=generated_response)
    else:
        return render_template("/feedback.html")

@home.route("/thankyou")
def thankpage():
    return render_template("/thankyou.html")
