import os, openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key  = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

MODEL_ID = "google/gemini-flash-1.5"

                                

def review_chapter(text: str) -> str:
    """Provide editorial feedback and refinements."""
    response = openai.ChatCompletion.create(
        model   = MODEL_ID,
        messages=[
            {"role": "system",
             "content": "You are a seasoned editor. Improve grammar, flow and "
                         "tone. Suggest concise edits where helpful."},
            {"role": "user", "content": text}
        ],
        temperature = 0.3
    )
    return response["choices"][0]["message"]["content"].strip()
