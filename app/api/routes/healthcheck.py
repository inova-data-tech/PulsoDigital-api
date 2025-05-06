from fastapi import APIRouter

router = APIRouter(
    prefix="/api/healthcheck",
    tags=["Healthcheck",]
)

@router.get("/", status_code=200)
def healthcheck():
    return {"status": "healthy"}
