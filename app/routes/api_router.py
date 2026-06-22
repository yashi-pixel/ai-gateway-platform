from fastapi import APIRouter, HTTPException
from app.services.generate_logic import Generateservice
from app.models.generate import GenerateRequest, GenerateResponse 

router=APIRouter()
services=Generateservice()

@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    try:
       result = await services.m_services(req.prompt)
       return {"response" : result}
    except Exception:
        raise  HTTPException(
            status_code=503,
            detail="Provider temporarily unavailable. Please try again later.",
        )
           