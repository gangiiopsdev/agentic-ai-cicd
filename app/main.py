from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        response = ping(host)
        return response
    except Exception as e:
        return {'error': str(e)}, 500