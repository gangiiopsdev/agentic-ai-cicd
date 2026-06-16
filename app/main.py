from fastapi import FastAPI
import subprocess
import shlex
def callable_ping(host):
    if not all(c.isalnum() for c in host):  # Simple validation to prevent special characters
        return "Invalid host"
    return subprocess.call(shlex.split(f'ping {host}'))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = callable_ping(host)
    if isinstance(result, str):
        return {"status": result}
    else:
        return {"status": "completed", "ping_result": result}