from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    if not request.host.isdigit():
        return JSONResponse(status_code=400, content={'status': 'error', 'message': 'Invalid input'})
    try:
        result = subprocess.run(['ping', '-c', str(request.host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={'status': 'error', 'message': str(e)})

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}