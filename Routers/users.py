from fastapi import APIRouter

router = APIRouter()


@router.get("/user", tags=["user"])
async def user():
    return {"messege": "user"}