from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    subprocess.call(shlex.split(f"ping {safe_host}"))
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    subprocess.call(shlex.split(f"ping {safe_host}"))
    return {"status": "completed"}