from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str
generate_ping_command = ['ping', '{host}']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.post("/ping")
def ping(request: PingRequest):
    # Sanitize input to prevent command injection
    sanitized_host = subprocess.quote(request.host)
    result = subprocess.run(generate_ping_command.format(host=sanitized_host), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}