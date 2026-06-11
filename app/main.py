from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with args, ensuring safe handling of user input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}