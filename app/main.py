from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host):
    if 'ping' in host:
        raise ValueError('Invalid host')
    subprocess.run(["ping", host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):
    try:
        return _ping(host)
    except Exception as e:
        return {'error': str(e)}, 400

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}