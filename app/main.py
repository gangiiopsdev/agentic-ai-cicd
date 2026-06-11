from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9._-]{1,255}$', host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.call(args)
    return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "result": result}
    except ValueError as e:
        return {"error": str(e)}