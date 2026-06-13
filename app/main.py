from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelisted set of hosts
    allowed_hosts = {'google.com', 'example.com'}
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Host not allowed')
    return {"status": "completed"}