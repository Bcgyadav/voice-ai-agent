import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a healthcare voice assistant.

Extract structured data from user input.

Return ONLY valid JSON. No explanation.

Schema:
{
  "intent": "book | cancel | reschedule | check",
  "doctor": "string or null",
  "date": "string or null",
  "time": "string or null"
}
"""

def process_user_input(text: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    raw_output = response.choices[0].message.content

    try:
        parsed = json.loads(raw_output)
        return parsed
    except:
        return {
            "intent": "unknown",
            "doctor": None,
            "date": None,
            "time": None,
            "raw": raw_output
        }