from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['host1', 'host2']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_safe_hosts:
        try:
            result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        raise ValueError('Host not allowed')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}