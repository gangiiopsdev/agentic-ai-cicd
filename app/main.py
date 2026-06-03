from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 50:
        return {"error": "Invalid hostname"}
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
    }