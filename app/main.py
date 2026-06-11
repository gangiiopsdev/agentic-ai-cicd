from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum() or e in ['-', '.', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_host(host)
    subprocess.run(shlex.split(f'ping {sanitized_host}'))
    return {"status": "completed"}