from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return JSONResponse(status_code=400, content={"error": "Invalid input"})
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}