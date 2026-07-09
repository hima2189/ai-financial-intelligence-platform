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
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB in bytes
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
# Size Validation Function
# ======================================================
def validate_file_size(file: UploadFile):
    """
    Validate uploaded file size.
    """

    file.file.seek(0, 2)  # Move to the end of the file
    file_size = file.file.tell()  # Get the current position (size)
    file.file.seek(0)  # Reset pointer for the next operation

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File size exceeds the maximum limit of 20 MB."
        )

# ======================================================
# Unique Filename Generation Function
# ======================================================
def unique_filename(original_filename: str) -> str:
    """
    Generate a unique filename using UUID.
    """

    extension = Path(original_filename).suffix
    unique_id = uuid.uuid4().hex
    return f"{unique_id}{extension}"

# ======================================================
# Save File Function
# ======================================================
def save_file(file: UploadFile, destination: Path):
    """
    Save the uploaded file to the specified destination.
    """

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

# ======================================================
# Upload Service
# ======================================================

async def process_upload(file: UploadFile):

    # Check filename exists
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )

    # Validate file extension
    validate_extension(file.filename)

    # Validate file size
    validate_file_size(file)

    # Generate unique filename
    generated_filename = unique_filename(file.filename)

    # Full destination path
    file_path = UPLOAD_DIR / generated_filename

    # Save uploaded file
    save_file(file, file_path)

    # Return response
    return {
        "filename": file.filename,
        "saved_as": generated_filename,
        "content_type": file.content_type,
        "location": str(file_path)
    }