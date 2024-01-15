# Import key libraries and packages
from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
from model import compose_response

app = FastAPI(title="AIP Course Submission")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()
app.include_router(router)

@app.get("/", response_class=JSONResponse)
async def heart_beat_check():
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={
            "message": "Heart beat message"}
    )


@app.post("/send", response_class=JSONResponse)
async def encode(query: str):
    resp = str(compose_response(query))
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": resp
        },
    )
