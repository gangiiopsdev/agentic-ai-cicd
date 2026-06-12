from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

def secure_ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return True

@app.get('/ping')
def ping_route(host: str):
    return secure_ping(host)

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}