from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isnumeric():
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)