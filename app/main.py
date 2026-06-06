from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not all(char.isalnum() for char in host):  # Basic validation of input
        raise ValueError('Invalid host name')
    return subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result}