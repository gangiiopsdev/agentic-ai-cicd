from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 50:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ping', result.stderr)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    return {"status": "completed"}