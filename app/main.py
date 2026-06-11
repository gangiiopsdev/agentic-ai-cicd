from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() or len(host) != 3:
        return {'status': 'failed', 'error': 'Invalid hostname format'}
    try:
        output = subprocess.run(['ping', os.path.join('/sbin', 'ping'), host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}