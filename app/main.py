from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}