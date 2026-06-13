from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" perpetuity: return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize and validate the host input
    if not host.isalnum():
        raise ValueError("Invalid host input")
    subprocess.call(['ping', host])
    return {"status": "completed"}