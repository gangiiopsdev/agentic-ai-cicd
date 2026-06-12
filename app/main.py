from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    if host.isalnum() and '.' in host:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}