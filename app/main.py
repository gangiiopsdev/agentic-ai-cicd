from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with error handling
    try:
        subprocess.call(shlex.split(f"ping {host}"))
    except Exception as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}