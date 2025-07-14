import os, openai
from dotenv import load_dotenv

load_dotenv()                                              # ← loads the .env file

# --- OpenRouter config ---
openai.api_key  = os.getenv("OPENROUTER_API_KEY")          # pulled securely
openai.api_base = "https://openrouter.ai/api/v1"           # MUST point to OpenRouter

MODEL_ID = "google/gemini-flash-1.5"

                                   

def rewrite_chapter(text: str) -> str:
    """Spin/modern‑rewrite a chapter."""
    response = openai.ChatCompletion.create(
        model   = MODEL_ID,
        messages=[
            {"role": "system",
             "content": "You are an energetic novelist. Rewrite the user text "
                         "to sound modern and engaging but keep plot and facts."},
            {"role": "user", "content": text}
        ],
        temperature = 0.7
    )
    return response["choices"][0]["message"]["content"].strip()
