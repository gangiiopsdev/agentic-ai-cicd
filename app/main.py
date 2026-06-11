from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> PingResponse:
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return PingResponse(status="Invalid input")

    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return PingResponse(status="completed with output: " + output.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status="failed with error: " + str(e))

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}