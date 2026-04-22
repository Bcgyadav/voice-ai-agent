from fastapi import APIRouter
from agent.llm_agent import process_user_input
from scheduler.appointment_engine import (
    check_availability,
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

router = APIRouter()

@router.post("/process")
def process(text: str):

    data = process_user_input(text)

    intent = data.get("intent")

    if intent == "book":
        slots = check_availability(data["doctor"], data["date"])
        return {
            "intent": intent,
            "available_slots": slots
        }

    elif intent == "cancel":
        result = cancel_appointment(data)
        return {"intent": intent, "response": result}

    elif intent == "reschedule":
        result = reschedule_appointment(data)
        return {"intent": intent, "response": result}

    elif intent == "check":
        slots = check_availability(data["doctor"], data["date"])
        return {"intent": intent, "available_slots": slots}

    return {
        "intent": "unknown",
        "message": "Could not understand request"
    }