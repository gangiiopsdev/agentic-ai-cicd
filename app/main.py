from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and args parameter
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}