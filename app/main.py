from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com']  # List of allowed hosts
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], shell=False, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ['example.com']:
        return safe_ping(host)
    else:
        raise ValueError('Host not allowed')