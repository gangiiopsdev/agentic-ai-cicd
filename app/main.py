from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host.isalnum() or '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid host input')
    return subprocess.list2cmdline([host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    host = sanitize_host()

    # Secure implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}