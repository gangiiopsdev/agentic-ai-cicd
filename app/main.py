from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not any(char in host for char in [';', '&', '|', '<', '>', '$', '`']):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid input'}