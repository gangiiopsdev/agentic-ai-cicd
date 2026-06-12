from fastapi import FastAPI
import subprocess
global host_whitelist = ['example.com', 'test.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in host_whitelist:
        # Secure implementation using subprocess.run with a list of arguments
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Host not allowed')