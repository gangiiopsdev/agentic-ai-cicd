from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not all(arg.isalnum() or arg in '-.' for arg in args[1:]):
        raise ValueError('Invalid host name')
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not all(arg.isalnum() or arg in '-.' for arg in args[1:]):
        raise ValueError('Invalid host name')
    subprocess.run(args, check=True, capture_output=True)