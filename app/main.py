from fastapi import FastAPI
import subprocess
import shlex
global app 
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        subprocess.call(shlex.split(f'ping {shlex.quote(host)}'))
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}