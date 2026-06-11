from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}