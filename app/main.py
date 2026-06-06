from fastapi import FastAPI
import subprocess
from shlex import quote as safe_quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize host input
    safe_host = safe_quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {'status': 'completed'}