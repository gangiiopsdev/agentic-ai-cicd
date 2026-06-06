from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with full executable path
    try:
        subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, str):
        return {"status": "error", "message": result}
    else:
        return {"status": "completed"}