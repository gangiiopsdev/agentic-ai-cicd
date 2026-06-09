from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex
    command_parts = ['ping', host]
    subprocess.call(command_parts)
    return {"status": "completed"}