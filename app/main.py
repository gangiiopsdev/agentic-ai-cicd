from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/)
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not all(c.isalnum() or c in [',', '.', '-', '_', ' '] for c in host):
        return {"status": "failed", "reason": "Invalid characters in hostname"}
    subprocess.call(['ping', host])
    return {"status": "completed"}