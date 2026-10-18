import os
from openai import OpenAI

BASE_URL = "https://api.groq.com/openai/v1"
MODEL = "openai/gpt-oss-120b"

api_key = os.getenv("AI_API_KEY")

if not api_key:
    raise RuntimeError("AI_API_KEY is not configured.")


client = OpenAI(api_key=api_key, base_url=BASE_URL)

'''
# print the models
for m in client.models.list():
    print(m.id)
'''

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain what revenue means in business in two sentences."}],
)

print(response.choices[0].message.content)

# To see everything at once
print(response.model_dump_json(indent=2))