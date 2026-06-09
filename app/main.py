from fastapi import FastAPI
import subprocess

globals = {'__builtins__': None}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    safe_host = subprocess.quote(host)
    try:
        subprocess.run(['ping', safe_host], check=True, timeout=5)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}