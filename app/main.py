from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "output": "Ping operation timed out."}