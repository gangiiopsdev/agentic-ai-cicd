from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.post="/ping"
def ping(request: PingRequest): 
    try:
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}