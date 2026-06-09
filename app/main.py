from fastapi import FastAPI
import subprocess32 as subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess32 for better compatibility and more features
    if host.startswith('192.168.') or host.startswith('10.'):  # Example of a simple validation
        try:
            output = subprocess32.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess32.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}