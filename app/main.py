from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or implement input validation
        if host not in ['localhost', '127.0.0.1']:
            return {'status': 'failed', 'error': 'Unauthorized host'}
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}