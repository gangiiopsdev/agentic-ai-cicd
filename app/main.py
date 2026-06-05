from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if host.startswith('-'):  # Example of input validation
        raise ValueError('Invalid input detected')
    subprocess.call(args)

    return {'status': 'completed'}