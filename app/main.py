from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host == 'localhost':
        return {'status': 'completed', 'output': 'Pong'}
    else:
        raise ValueError('Unsafe host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', safe_ping(host)], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}