import os
import requests

def call_openrouter():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Please set OPENROUTER_API_KEY environment variable")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Placeholder ko valid URL se replace kiya
        "X-Title": "OpenRouter Haiku Example"
    }
    data = {
        "model": "google/gemini-flash-1.5:free",
        "messages": [
            {"role": "user", "content": "Write a haiku about the moon."}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(result["choices"][0]["message"]["content"])

if __name__ == "__main__":
    call_openrouter()