from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        response = requests.get(f'http://{request.host}/ping', timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}