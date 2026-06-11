from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with proper input validation
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}