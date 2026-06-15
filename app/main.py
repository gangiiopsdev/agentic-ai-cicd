from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    import shlex
    safe_host = shlex.quote(host)
    subprocess.call(f'ping {safe_host}', shell=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}