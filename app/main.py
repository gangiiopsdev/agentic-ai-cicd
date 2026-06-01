from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ALLOWED_HOSTS:
        # Validate and sanitize the input
        subprocess.run(['ping', '-c', str(1)], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}, 403