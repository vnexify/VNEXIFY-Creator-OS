from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def api_health():
    return {
        "status": "ok",
        "version": "0.1"
    }

@router.get("/status")
def status():
    return {
        "status": "ok",
        "service": "vnexify backend"
    }
