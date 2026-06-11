from pydantic import BaseModel
#validating the incoming and outgoing data with specified schema

class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    response: str