from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host or len(host) > 255:
        return {'error': 'Invalid host input'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}