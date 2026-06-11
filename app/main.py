from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = host.replace(';', '').replace('&', '')
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}