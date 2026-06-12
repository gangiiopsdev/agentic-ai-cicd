from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}