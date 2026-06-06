from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True, shell=False)
        return {
            'status': 'completed',
            'output': result.stdout,
            'stderr': result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            'status': 'failed',
            'error': str(e)
        }