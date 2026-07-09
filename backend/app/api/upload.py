from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import process_upload

router = APIRouter(
    prefix="/api/v1/upload",
    tags=["Document Upload"]
)

@router.get("/")
def upload_status():
    return {
        "status": "Upload API is Ready"
    }

@router.post("/")
async def upload_document(
        file: UploadFile = File(...)
):
    return await process_upload(file)