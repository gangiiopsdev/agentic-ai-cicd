from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and escaping
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}