import os
from openai import OpenAI


def call_llm(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return """
        {
            "requirements" : ["Accept a customer inquiry payload", 
            "Store the inquiry"
            "Return a success response"],
            "assumptions" : ["SQLite or in-memory storage is acceptable"],
            "tasks" : ["Create FastAPI endpoint",
                       "Validate request payload",
                       "Persist inquiry",
                       "Return response"]
        }"""
    
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a senior software engineer and systems architect."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content or ""