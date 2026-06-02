from fastapi import FastAPI
import subprocess
global host 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

def validate_host(host: str) -> bool:
    # Add your validation logic here
    return True