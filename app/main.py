from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if all(c.isalnum() or c in ('-', '.', '_') for c in host):  # Basic validation of the hostname
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid hostname'}, 400