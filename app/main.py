from fastapi import FastAPI
from app.routes.api_router import router

app = FastAPI()
app.include_router(router)

@app.get("/root")
def root():
    return {
        "status":"warning"
    }