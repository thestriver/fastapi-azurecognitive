from typing import List
from fastapi import FastAPI
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from utils import get_text_analytics_credentials

app = FastAPI()

load_dotenv()
key, endpoint = get_text_analytics_credentials()

credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(
    endpoint=endpoint, credential=credential)


@app.post("/")
async def analyze_texts(texts: List[str]):
    sentiment_response = text_analytics_client.analyze_sentiment(texts)
    key_phrase_response = text_analytics_client.extract_key_phrases(texts)
    language_response = text_analytics_client.detect_language(texts)

    sentiment_sentiments = []
    for result in sentiment_response:
        if not result.is_error:
            sentiment = {"sentiment": result.sentiment,
                         "confidence_scores": result.confidence_scores}
            sentiment_sentiments.append(sentiment)

    key_phrases = []
    for result in key_phrase_response:
        if not result.is_error:
            key_phrases.append(result.key_phrases)

    detected_languages = []
    for result in language_response:
        if not result.is_error:
            detected_languages.append(result.primary_language.iso6391_name)

    return {"sentiments": sentiment_sentiments, "key_phrases": key_phrases, "detected_languages": detected_languages}
