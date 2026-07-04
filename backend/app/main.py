from fastapi import FastAPI

app = FastAPI(
    title="AI Financial Intelligence Platform",
    description="Enterprise AI Financial Document Intelligence Platform",
    version="1.0.0",
)


@app.get("/")
def health():
    return {
        "status": "success",
        "message": "AI Financial Intelligence Platform is running 🚀"
    }