from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        command = ['ping', host]
        subprocess.call(command, shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500