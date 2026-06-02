from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if 'ping' in host:
        raise ValueError('Host contains disallowed keyword')
    return host

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    host = validate_host(host)
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}