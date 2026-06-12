from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        raise HTTPException(status_code=403, detail='Unauthorized host')
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}