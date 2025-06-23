import os
from litellm import completion

def call_litellm():
    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
    if not os.environ["OPENROUTER_API_KEY"]:
        raise ValueError("Please set OPENROUTER_API_KEY environment variable")

    response = completion(
        model="openrouter/google/gemini-flash-1.5:free",
        messages=[
            {"role": "user", "content": "Tell me a joke about programming."}
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    call_litellm()