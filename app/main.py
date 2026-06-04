from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum() and not all(char in string.printable for char in host):
        return {'status': 'failed', 'message': 'Invalid host input'}
    args = ['ping', host]
    result = subprocess.call(args)
    return {'status': 'completed' if result == 0 else 'failed'}