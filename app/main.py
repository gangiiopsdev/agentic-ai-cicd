from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in '._-@' for c in host):  # Basic validation of input
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True, shell=False)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}