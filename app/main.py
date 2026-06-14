from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = f'ping -c 1 {host}'  # Limiting the number of pings to prevent DoS attacks
    args = shlex.split(command)
    subprocess.run(args, check=True)  # Using run instead of call for better error handling
    return {"status": "completed"}