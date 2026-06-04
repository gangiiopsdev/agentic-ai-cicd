from fastapi import FastAPI
import subprocess
import socket

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

def safe_ping(host: str):
    try:
        ip = socket.gethostbyname(host)
        if ip not in ALLOWED_IPS:
            return "Invalid host"
    except socket.gaierror:
        return "Invalid host"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}