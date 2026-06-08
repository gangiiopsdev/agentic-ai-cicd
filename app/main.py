from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Host not allowed')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        if validate_host(host):
            subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}