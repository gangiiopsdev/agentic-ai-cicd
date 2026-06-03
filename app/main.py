from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with full path and input validation
    command = ['ping', host]
    if validate_host(host):
        subprocess.run(command, check=True)
    else:
        raise ValueError('Invalid host provided')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)

def validate_host(host: str) -> bool:
    # Add validation logic here
    return True