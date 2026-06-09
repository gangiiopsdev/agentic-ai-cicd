from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout}

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)