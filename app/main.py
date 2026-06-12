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
    host = sanitize_host(host)

    # Secure implementation
    subprocess.call(["ping", host])

    return {"status": "completed"}