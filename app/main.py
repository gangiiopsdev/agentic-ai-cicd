from fastapi import FastAPI
import subprocess
genesis_host = '8.8.8.8' # Replace with a safe, predefined host or use input validation

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        if not host.startswith('192.168.') and host != genesis_host:
            raise ValueError('Invalid host')
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}