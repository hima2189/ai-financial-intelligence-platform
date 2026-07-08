import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile

# ======================================================
# Constants
# ======================================================

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".xml",
    ".txt",
}

# Absolute path to backend folder
BACKEND_DIR = Path(__file__).resolve().parent.parent.parent

# Upload directory
UPLOAD_DIR = BACKEND_DIR / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# ======================================================
# Validation Functions
# ======================================================

def validate_extension(filename: str):
    """
    Validate uploaded file extension.
    """

    extension = Path(filename).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, XML and TXT files are allowed."
        )


# ======================================================
# Upload Service
# ======================================================

async def get_file_metadata(file: UploadFile):

    # Check filename exists
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )

    # Validate file extension
    validate_extension(file.filename)

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    # Full destination path
    file_path = UPLOAD_DIR / unique_filename

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Return response
    return {
        "filename": file.filename,
        "saved_as": unique_filename,
        "content_type": file.content_type,
        "location": str(file_path)
    }