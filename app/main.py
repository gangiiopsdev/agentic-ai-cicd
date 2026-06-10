from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        subprocess.run(['ping', host], check=True, shell=False, capture_output=True, text=True)
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': f'Ping failed: {e}'}

    output = {
        'status': 'completed'
    }
    if subprocess.run(['ping', host], check=False, shell=False, capture_output=True, text=True).stdout:
        output['output'] = subprocess.run(['ping', host], check=False, shell=False, capture_output=True, text=True).stdout
    return output