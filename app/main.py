from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):\n    try:\n        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except subprocess.CalledProcessError as e:\n        return JSONResponse(status_code=400, content={'status': 'error', 'message': str(e)})

@app.get("/")
def home():\n    return {"message": "Agentic Self-Healing Pipeline"}