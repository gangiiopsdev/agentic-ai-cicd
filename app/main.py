from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True)
    return result.stdout

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)

@app.get("/ping")
def ping_endpoint(host: str):
    return safe_ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}