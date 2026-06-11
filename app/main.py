from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    subprocess.run(['ping', safe_host], check=True)

    return {'status': 'completed'}