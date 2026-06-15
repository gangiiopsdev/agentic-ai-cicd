from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement validation logic here (e.g., whitelist of allowed hosts)
    return host in ['example.com', 'test.example.com']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        command = ['ping', host]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')