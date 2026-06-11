from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(c in allowed_chars for c in host) and len(host) <= 63

@app.get("/ping")
def ping(request: PingRequest):
    if validate_host(request.host):
        # Use subprocess.run with shell=False for better security
        result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid input"}