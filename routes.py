
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "running"}

@router.get("/live-stats")
def stats():
    return {"entries": 0, "income": 0}
