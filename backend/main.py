from fastapi import FastAPI
from backend.routes.health import router as health_router
from backend.routes.stt import router as stt_router
from backend.routes.agent import router as agent_router

app = FastAPI()

app.include_router(health_router)
app.include_router(stt_router)
app.include_router(agent_router)

@app.get("/")
def root():
    return {"message": "Voice AI Agent running"}