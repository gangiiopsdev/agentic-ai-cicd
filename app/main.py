from fastapi import FastAPI
import subprocess
import shlex

global ping

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Use shlex to safely handle the host input
        args = ['ping'] + shlex.split(host)
        subprocess.call(args, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}