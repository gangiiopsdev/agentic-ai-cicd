from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping/{host:path}")
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid host parameter")
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)  # Use run instead of call for better error handling
    return {"status": "completed"}