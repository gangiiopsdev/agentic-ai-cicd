from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Define allowed characters and length
    return all(c.isalnum() or c in '._-' for c in host) and len(host) <= 64

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)  # Removed shell=False as it's not necessary here
    return {"status": "completed"}