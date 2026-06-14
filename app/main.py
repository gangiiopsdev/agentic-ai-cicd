from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    if subprocess.call(['ping', host], shell=False) != 0:
        raise Exception("Ping failed")

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping_fixed(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    if subprocess.call(['ping', host], shell=False) != 0:
        raise Exception("Ping failed")
    return {"status": "completed"}