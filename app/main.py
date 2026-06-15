from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

def validate_host(host):
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Safe implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}