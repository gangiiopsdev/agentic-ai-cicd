from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = ["ping", host]
    result = subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode() if result.returncode == 0 else result.stderr.decode()}