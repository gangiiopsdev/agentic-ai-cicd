from fastapi import FastAPI
import subprocess
from pydantic import validator
def ping(host: str = Depends(PingCommand.validate_host)):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.stderr)}
global_host_whitelist = {'8.8.8.8', '127.0.0.1'}
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in global_host_whitelist:
        raise ValueError('Invalid host')
    return ping(host)