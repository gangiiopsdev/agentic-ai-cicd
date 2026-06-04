from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    try:
        subprocess.call(['ping', host])
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}