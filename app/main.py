from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid input for ping')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}