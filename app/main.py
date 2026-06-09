from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ["ping", host]
    result = subprocess.run(shlex.split(host), check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode() if result.returncode == 0 else result.stderr.decode()}