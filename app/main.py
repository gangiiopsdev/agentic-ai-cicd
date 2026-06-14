from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with argument validation and sanitization
    if not host.isalnum() or len(host) > 128:
        raise ValueError("Invalid hostname")
    subprocess.call(['ping', host])
    return JSONResponse(content={"status": "completed"})