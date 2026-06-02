from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not valid_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', shlex.quote(host)], shell=False)
def valid_host(host):
    return all(c.isalnum() or c in ('-', '.', '_') for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}