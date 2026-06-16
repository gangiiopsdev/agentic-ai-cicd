from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)