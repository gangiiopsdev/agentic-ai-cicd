from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with input sanitization
        if host and all(c.isalnum() or c in ('-', '.', ':') for c in host):  # Basic validation
            result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        else:
            return {'status': 'error', 'output': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr.decode('utf-8')}