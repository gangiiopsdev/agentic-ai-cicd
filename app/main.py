from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using shlex.split to prevent command injection
        subprocess.call(shlex.split(f"ping {host}"))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}