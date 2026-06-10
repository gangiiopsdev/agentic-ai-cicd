from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}