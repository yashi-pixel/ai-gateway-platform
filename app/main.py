from fastapi import FastAPI
from app.routes.api_router import router

app = FastAPI()
app.include_router(router)

@app.get("/health")
def root():
    return {
        "status":"healthy"
    }