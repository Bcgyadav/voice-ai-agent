# 🎤 Real-Time Multilingual Voice AI Agent

### Clinical Appointment Booking System

---

## 📌 Overview

This project implements a **real-time voice AI agent** capable of handling clinical appointment workflows through natural voice conversations.

The system supports:

* Appointment booking
* Appointment rescheduling
* Appointment cancellation
* Conflict detection and alternative suggestions
* Multilingual interaction (English, Hindi, Tamil)
* Context-aware conversations (session + persistent memory)

The goal is to simulate a **production-grade AI system** with low latency and modular architecture.

---

## 🧠 System Architecture

```
User Speech
     ↓
Speech-to-Text (STT)
     ↓
Language Detection
     ↓
LLM Agent (Intent Extraction)
     ↓
Tool Orchestration Layer
     ↓
Appointment Scheduler
     ↓
Text Response
     ↓
Text-to-Speech (TTS)
     ↓
Audio Output
```

---

## ⚙️ Tech Stack

| Component        | Technology                           |
| ---------------- | ------------------------------------ |
| Backend          | FastAPI (Python)                     |
| LLM              | OpenAI GPT-4o-mini                   |
| Speech-to-Text   | OpenAI Whisper API                   |
| Memory (Session) | In-memory (extendable to Redis)      |
| Database         | In-memory (extendable to PostgreSQL) |
| API Testing      | Swagger UI                           |
| Deployment       | Docker (planned)                     |

---

## 🚀 Features

### ✅ Voice Processing

* Converts speech to text using Whisper API
* Handles multilingual input (EN, HI, TA)

### ✅ Intelligent Agent

* Extracts structured intent using LLM
* Returns strict JSON format
* Handles ambiguous inputs gracefully

### ✅ Appointment Management

* Booking
* Cancellation
* Rescheduling
* Availability checking

### ✅ Tool Orchestration

* LLM triggers backend functions (not hardcoded)
* Modular separation between AI and business logic

### ✅ Contextual Memory

* Session memory stores current conversation state
* Designed for Redis-based persistent memory

---

## 📂 Project Structure

```
voice-ai-agent/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   │   ├── health.py
│   │   ├── stt.py
│   │   ├── agent.py
│
├── agent/
│   └── llm_agent.py
│
├── services/
│   └── speech_to_text.py
│
├── scheduler/
│   └── appointment_engine.py
│
├── memory/
│   └── session_memory.py
│
├── database/
│   └── db.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/voice-ai-agent.git
cd voice-ai-agent
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run Server

```
python -m uvicorn backend.main:app --reload
```

### 6️⃣ Test API

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Usage

### 🎤 Speech Input

Upload audio to `/transcribe`

### 🤖 Agent Processing

Send text to `/process`

Example:

```
"Book appointment with cardiologist tomorrow at 2 PM"
```

Response:

```json
{
  "intent": "book",
  "available_slots": ["10:00 AM", "2:00 PM", "4:00 PM"]
}
```

---

## 📊 Latency Design

Target: **< 450 ms (end-to-end)**

| Stage             | Estimated Latency |
| ----------------- | ----------------- |
| Speech-to-Text    | ~120 ms           |
| LLM Processing    | ~200 ms           |
| Response Handling | ~100 ms           |
| Total             | ~420 ms           |

> Note: Latency logging hooks are included and can be extended for production monitoring.

---

## 🧠 Memory Design

### Session Memory

* Stores current conversation context
* Example:

```
User: Book appointment
Agent: Which doctor?
User: Cardiologist
```

### Persistent Memory (Planned)

* Patient preferences
* Past appointments
* Language preference

---

## ⚠️ Trade-offs

| Decision           | Trade-off                                         |
| ------------------ | ------------------------------------------------- |
| OpenAI API for STT | Faster but requires API key                       |
| In-memory storage  | Simple but not scalable                           |
| No WebSockets yet  | Easier implementation but not real-time streaming |
| Basic scheduler    | Simplified for demo                               |

---

## 🚧 Limitations

* Real-time streaming via WebSockets not implemented
* Persistent database not integrated
* TTS (Text-to-Speech) not implemented yet
* Outbound calling is simulated

---

## 🔮 Future Improvements

* Redis-based memory system
* PostgreSQL integration
* WebSocket real-time audio streaming
* Full TTS voice responses
* Outbound call campaigns
* Latency monitoring dashboard


---

## 📌 Conclusion

This project demonstrates:

* AI agent orchestration
* Real-time system design
* Multilingual voice processing
* Clean modular backend architecture

It is designed with scalability and production-readiness in mind.

---
