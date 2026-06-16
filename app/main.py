from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isdigit():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout, "stderr": result.stderr}
    except ValueError as e:
        return {"error": str(e)}