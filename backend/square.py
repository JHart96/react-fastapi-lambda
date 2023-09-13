from fastapi import APIRouter

router = APIRouter()

@router.get("/square/{x}")
def square(x: int):
    return {"message": str(x**2)}