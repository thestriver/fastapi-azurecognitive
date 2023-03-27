# fastapi-azurecognitive

An API (using Python's FastAPI) that runs Sentiment, Language Detection and Key Phrase extraction analysis on provided array of texts using Azure Cognitive Service.

Run 
```python
uvicorn main:app --reload
````

Test it using: 
- http://127.0.0.1:8000/docs/
- Sample request:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '["Great atmosphere. Close to plenty of restaurants, hotels, and transit! Staff are friendly and helpful.", "Bad atmosphere. Not close to plenty of restaurants, hotels, and transit! Staff are not friendly and helpful.", "This book is amazing!", "Ce document est rédigé en Français."]'

```

Sample API response:

```python
{
  "sentiments": [
    {
      "sentiment": "positive",
      "confidence_scores": {
        "positive": 1,
        "neutral": 0,
        "negative": 0
      }
    },
    {
      "sentiment": "negative",
      "confidence_scores": {
        "positive": 0,
        "neutral": 0,
        "negative": 1
      }
    },
    {
      "sentiment": "positive",
      "confidence_scores": {
        "positive": 1,
        "neutral": 0,
        "negative": 0
      }
    },
    {
      "sentiment": "neutral",
      "confidence_scores": {
        "positive": 0.02,
        "neutral": 0.97,
        "negative": 0.01
      }
    }
  ],
  "key_phrases": [
    [
      "Great atmosphere",
      "plenty",
      "restaurants",
      "hotels",
      "transit",
      "Staff"
    ],
    [
      "Bad atmosphere",
      "plenty",
      "restaurants",
      "hotels",
      "transit",
      "Staff"
    ],
    [
      "book"
    ],
    [
      "Français",
      "document"
    ]
  ],
  "detected_languages": [
    "en",
    "en",
    "en",
    "fr"
  ]
}
```

