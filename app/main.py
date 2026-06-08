from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping -c 4 {host}')  # Limiting the number of pings for security
    subprocess.run(args, check=True)
    return {"status": "completed"}