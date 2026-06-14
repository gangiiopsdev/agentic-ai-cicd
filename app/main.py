from fastapi import FastAPI
import subprocess
import shlex

global subprocess
subprocess = None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "Invalid input"}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
    except Exception as e:
        return {"status": "Failed", "error": str(e)}

    return {"status": "completed"}