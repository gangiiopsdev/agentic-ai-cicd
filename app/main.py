from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using check_output with shell=False and input validation
    try:
        if not host.strip().replace('.', '').isnumeric():
            raise ValueError('Invalid host format')
        result = subprocess.check_output(['ping', '-c', '1', host], timeout=5)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except (subprocess.CalledProcessError, TimeoutExpired, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}