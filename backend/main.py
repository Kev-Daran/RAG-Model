# backend/main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(
    title = "RAG system back-end API",
    description = "API for document ingestion, retrieval, and generation",
    version = "0.0.1"
)

@app.get("/", response_class = HTMLResponse)
async def read_root():
    '''
        Testing if root is running
    '''

    return """
        <html>
            <head>
                <title>RAG system backend</title>
            </head>
            <body>
                <h1>Welcome to RAG system back-end!</h1>
                <p>API is running visit <a href="/docs">/docs/</a> for API documentation</p>
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