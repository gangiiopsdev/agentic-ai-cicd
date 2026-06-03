from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}

# Preventive Controls
# 1. Validate and sanitize user input to ensure it does not contain malicious content.
# 2. Use `subprocess.run` with `shell=False` and avoid using shell=True unless absolutely necessary.