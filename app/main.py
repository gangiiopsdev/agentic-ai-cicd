from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/home')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit() or len(host) > 15:
        return {"error": "Invalid host"}
    args = shlex.split(f'ping -c 4 {host}')
    try:
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}