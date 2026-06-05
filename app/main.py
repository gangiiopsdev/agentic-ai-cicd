from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.post("/ping")
def ping(request: PingRequest): 
    # Sanitize user input to prevent command injection
    if not request.host.isalnum() and '-' not in request.host:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.run(['ping', '-c 1', str(request.host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}