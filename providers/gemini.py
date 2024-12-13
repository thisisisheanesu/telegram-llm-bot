import requests
import os

api_key = os.getenv('GEMINI_API_KEY')

def call_gemini_api(prompt):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    response = requests.post(
        f"{url}?key={api_key}",
        headers=headers,
        json=data
    )

    try:
        message = response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        message = "Something went wrong. This may be due to rate limiting or other issues."
    
    return message
