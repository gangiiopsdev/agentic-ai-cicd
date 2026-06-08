from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    if host in ['example.com', '127.0.0.1']:  # Whitelist of allowed hosts
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        execute_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}