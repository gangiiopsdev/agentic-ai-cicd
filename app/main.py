from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = host.replace(';', '').replace('&', '')
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}