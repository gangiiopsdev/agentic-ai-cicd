from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using shlex.quote
    from shlex import quote
    safe_host = quote(host)
    subprocess.call(f"ping {safe_host}")
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping_safe(host: str):
    safe_host = quote(host)
    subprocess.call(f"ping {safe_host}")
    return {"status": "completed"}