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
    try:
        # Secure implementation using shlex.split to safely handle command arguments
        subprocess.call(shlex.split(f"ping {host}"))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500