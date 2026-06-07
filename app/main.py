from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Ensure input is validated or sanitized before passing to subprocess
    if not host.isalnum():
        raise ValueError('Invalid input')
    ping(host)
    return {"status": "completed"}