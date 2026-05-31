from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        SafeSubprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400