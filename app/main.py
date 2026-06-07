from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Secure implementation
    result = subprocess.call(['ping', host])

    return {'status': 'completed' if result == 0 else 'failed'}