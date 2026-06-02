from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use shlex to safely quote the command arguments
    safe_host = shlex.quote(host)
    command = ["ping", safe_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}