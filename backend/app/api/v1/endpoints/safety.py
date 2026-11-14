from fastapi import APIRouter
from app.services.safety_sentinel import VERIFIED_HELPLINES, NON_MEDICAL_DISCLAIMER

router = APIRouter()

@router.get("/helplines")
def get_helplines():
    return {
        "disclaimer": NON_MEDICAL_DISCLAIMER,
        "helplines": VERIFIED_HELPLINES
    }
