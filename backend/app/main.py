from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="AI Financial Intelligence Platform",
    description="Enterprise AI Financial Document Intelligence Platform",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "AI Financial Intelligence Platform is running 🚀",
    }