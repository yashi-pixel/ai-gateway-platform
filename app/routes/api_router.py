from fastapi import APIRouter
from app.services.generate_logic import Generateservice
from app.models.generate import GenerateRequest, GenerateResponse 

router=APIRouter()
services=Generateservice()

@router.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    try:
       result = await services.m_services(req.prompt)
       return {"response" : result}
    except:
           