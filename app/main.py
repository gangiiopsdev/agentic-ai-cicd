from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '@' in host:
        raise ValueError('Invalid input for hostname')
    result = safe_ping(host)
    return {"status": "completed", "output": result}