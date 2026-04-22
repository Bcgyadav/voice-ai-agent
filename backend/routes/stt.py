from fastapi import APIRouter, UploadFile, File
import shutil
from services.speech_to_text import transcribe_audio

router = APIRouter()

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe_audio(path)
    return {"text": text}