from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation
    if host in allowed_hosts:
        result = subprocess.run(['ping', '--'] + [host], capture_output=True, text=True)
        return {"status": result.stdout}
    else:
        raise ValueError('Unauthorized host')

allowed_hosts = {'example.com'}  # Define a list of allowed hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)