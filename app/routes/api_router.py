from fastapi import APIRouter
from app.services.generate_logic import Generatelogic
from app.models.generate import GenerateRequest, GenerateResponse 

router=APIRouter()
services=Generatelogic()

@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    result = await services.ser(req.prompt)
    return {"response" : result}