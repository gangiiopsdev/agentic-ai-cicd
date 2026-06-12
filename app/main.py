from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here (e.g., regex to match IP addresses or hostnames)
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"status": "Invalid host", "code": 400}