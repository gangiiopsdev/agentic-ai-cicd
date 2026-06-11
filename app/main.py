from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to avoid command injection
    if not is_valid_host(host):
        return {"status": "invalid_host", "message": "Invalid host provided"}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Simple validation to allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)