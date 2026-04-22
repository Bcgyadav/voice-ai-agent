import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 👈 ADD THIS

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(file_path):
    with open(file_path, "rb") as audio:
        result = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio
        )
    return result.text