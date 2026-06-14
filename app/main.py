from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Basic validation, improve as needed
    if not host or ' ' in host:
        raise ValueError("Invalid host")

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    is_valid_host(host)
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}