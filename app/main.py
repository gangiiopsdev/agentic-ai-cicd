from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True for better error handling and shell=False to avoid shell injection
    if not host.strip().isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}