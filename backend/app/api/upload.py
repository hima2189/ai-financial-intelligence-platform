from fastapi import APIRouter

router = APIRouter(
    prefix= "/api/v1/upload",
    tags= ["Document Upload"]
)

@router.get("/")
def upload_status ():
    """
    Health endpoint for Upload API
    """
    return {"status": "Upload API is Ready"}