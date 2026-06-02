from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    
    args = ['ping', host]
    subprocess.call(args)
    
    return {'status': 'completed'}