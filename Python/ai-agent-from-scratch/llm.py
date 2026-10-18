import os
from openai import OpenAI

# Shared LLM setup – every demo file imports client and MODEL from here.
MODEL = "openai/gpt-oss-120b"

api_key = os.getenv("AI_API_KEY")

if not api_key:
    raise RuntimeError("AI_API_KEY is not configured.")

client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
