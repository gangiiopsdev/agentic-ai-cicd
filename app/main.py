from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate host input (e.g., allow only IP addresses or domain names)
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input (e.g., allow only IP addresses or domain names)
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

    subprocess.run(['ping', host], check=True)