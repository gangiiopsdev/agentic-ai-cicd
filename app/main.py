from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # More comprehensive input validation and sanitization
    if not host.isalnum() or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}