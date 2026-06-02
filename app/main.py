from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = shlex.split(f'ping -c 1 {host}')
    try:
        subprocess.run(args, check=True)
        return {"status": "completed", "result": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}