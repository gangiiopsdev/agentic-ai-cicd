from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-_.')
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}