from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck", tags=["Healthcheck"], status_code=200)
def healthcheck():
    return {"status": "healthy"}
