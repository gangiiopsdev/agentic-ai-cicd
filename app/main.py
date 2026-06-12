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
        # Secure implementation using shlex.split to safely split the command
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500