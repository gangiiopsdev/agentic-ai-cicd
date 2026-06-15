from fastapi import FastAPI
import subprocess
globally_allowed_hosts = set(['example.com', 'localhost'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.call(f'ping {host}')
    else:
        return {"error": "Host not allowed"}
    return {"status": "completed"}