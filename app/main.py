from fastapi import FastAPI
import subprocess
def run_ping(host):
    # Secure implementation using shlex.quote to prevent command injection
    from shlex import quote
    subprocess.call(f'ping {quote(host)}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    run_ping(host)
    return {"status": "completed"}