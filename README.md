# 💬 Project 3 — AI Chat History API

A production-grade REST API with persistent chat history stored in a database!

## 📋 What It Does
- Chat with AI powered by Groq LLM
- Save every question and answer to SQLite database
- View full chat history anytime
- Data persists even after server restarts

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| FastAPI | REST API framework |
| SQLAlchemy | Database ORM |
| SQLite | Lightweight database |
| Pydantic | Data validation |
| Groq | AI language model |

## 📁 Project Structure
```
ai-chat-history/
│
├── app/
│   ├── main.py          # API entry point
│   ├── models.py        # Pydantic models
│   ├── config.py        # Settings & environment variables
│   ├── dbConnection.py  # Database connection
│   ├── db_models.py     # Database table structure
│   └── services/
│       └── llm_call.py  # Groq AI logic
│
├── .env
├── .gitignore
└── requirements.txt
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-chat-history.git
cd ai-chat-history
```

### 2. Create virtual environment
```bash
python -m venv env
env\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key
language_model=llama-3.3-70b-versatile
database_url=sqlite:///./chat_history.db
max_tokens=500
```

### 5. Run the API
```bash
uvicorn app.main:app --reload
```

### 6. Test the API
Visit → **http://127.0.0.1:8000/docs**

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/chat` | Send a message to AI |
| GET | `/history` | Get full chat history |

## 💡 Example Chat Request
```json
{
    "question": "What is Python used for?"
}
```

## 📊 Example Chat Response
```json
{
    "answer": "Python is used for web development, data science, AI...",
    "created_at": "2024-01-15T10:30:00"
}
```

## 📜 Example History Response
```json
[
    {
        "id": 1,
        "question": "What is Python?",
        "answer": "Python is a programming language...",
        "created_at": "2024-01-15T10:30:00"
    }
]
```

## 🗄️ Database
- Uses SQLite for simplicity
- Easily upgradeable to PostgreSQL by changing `database_url` in `.env`
