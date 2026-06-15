from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        subprocess.call(['ping', request.host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))