# backend/main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

@asynccontextmanager
async def lifespan(app : FastAPI):
    '''
        Context manager for application startup and shutdown
    '''

    print("Backend starting up...")

    global DATABASE_URL, CHROMA_HOST, CHROMA_PORT, GEMINI_API_KEY

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db") # Fallback for local testing
    CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
    CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8001")) # Convert to int
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") # Get Gemini API Key

    print(f"Attempting to connect to Postgres at: {DATABASE_URL}")
    print(f"Attempting to connect to ChromaDB ar: {CHROMA_HOST}:{CHROMA_PORT}")
    print(f"Gemini API key loaded: {'Yes' if GEMINI_API_KEY else 'No'}")

    yield # STARTUP phase complete

    print("Backend shutting down...")

app = FastAPI(
    title = "RAG system back-end API",
    description = "API for document ingestion, retrieval, and generation",
    version = "0.0.1",
    lifespan=lifespan
)

@app.get('/', response_class=HTMLResponse)
async def read_root():
    '''
        Root endpoint to confirm backend is running
    '''

    return f"""
    <html>
        <head>
            <title>RAG System backend</title>
        </head>
        <body>
            <h1>Welcome to RAG system backend!</h1>
            <p>API is running</p>
            <p>Postgresql URL: <code>{DATABASE_URL}</code></p>
            <p>ChromaDB Host:: <code>{CHROMA_HOST}:{CHROMA_PORT}</code></p>
            <p>Gemini API Key Loaded: <code>{'Yes' if GEMINI_API_KEY else 'No (or empty)'}</code></p>
            <p>Visit <a href="/docs">/docs</a> for API documentation</p>
        </body>
    </html>
    """

@app.get("/health")
async def health_check():
    '''
        Health check endpoint
    '''

    return {"status" : "ok", "message" : "backend is healthy!"}


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = 8000)