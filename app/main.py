from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid hostname')
    sanitized_host = subprocess.list2cmdline([host])
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output.decode('utf-8')}''