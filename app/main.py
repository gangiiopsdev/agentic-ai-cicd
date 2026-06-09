from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to ensure it only contains allowed characters (e.g., alphanumeric and hyphen)
    if not all(c.isalnum() or c == '-' for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}