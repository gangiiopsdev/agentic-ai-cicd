from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex to safely handle arguments
    args = ['ping', *shlex.split(host)]
    subprocess.call(args)
    return {"status": "completed"}