from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using shlex.split to split the command safely
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}