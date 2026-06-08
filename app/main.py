from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['example.com', 'localhost']
    if host in valid_hosts:
        try:
            output = subprocess.check_output(['ping', host], timeout=10)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)