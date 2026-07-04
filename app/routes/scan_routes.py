from fastapi import APIRouter
from app.controllers.scan_controller import scan_link

router = APIRouter()

@router.post("/scan-link")
async def scan(data: dict):
    return await scan_link(data["url"])
