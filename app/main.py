from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get(
    "/",
    summary="Agentic Self-Healing Pipeline"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    summary="Ping a host and get the response"
)
def ping(host: str):
    if not host or len(host) > 255 or ' ' in host:
        raise HTTPException(status_code=400, detail="Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}