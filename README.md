# Agentic Paper Assistant

This is a simple FastAPI project that exposes an endpoint `/ask?q=your_query` which returns an augmented answer from an openAI model.

## Running the server

```bash
uvicorn main:app --reload
```

Then visit: http://127.0.0.1:8000/ask?q=hello


