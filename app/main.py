from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.replace('.', '').replace('-', '').isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)