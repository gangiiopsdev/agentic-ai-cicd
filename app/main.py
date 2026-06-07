from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.call(shlex.split(f'ping {host}'), timeout=10)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}