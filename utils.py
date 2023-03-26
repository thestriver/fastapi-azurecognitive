import os


def get_text_analytics_credentials():
    key = os.environ.get("TEXT_ANALYTICS_API_KEY")
    endpoint = os.environ.get("TEXT_ANALYTICS_API_ENDPOINT")

    if not key or not endpoint:
        raise ValueError(
            "Please provide a Text Analytics API key and endpoint.")

    return key, endpoint
