from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if subprocess.call(['ping', host]) == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}