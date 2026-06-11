from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '-.')
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}