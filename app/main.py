from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum() or len(host) > 50:
        return{"error": "Invalid host name"}
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}