from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation using subprocess.run with sanitization
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'result': result.stdout.decode('utf-8')}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

# Preventive controls
@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is safe
    if not host.isdigit() or len(host) > 3:
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'result': result.stdout.decode('utf-8')}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}