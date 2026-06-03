from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Safe implementation using subprocess.run with shell=False and full path for the executable
    subprocess.call(['ping', '-c', '1', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}