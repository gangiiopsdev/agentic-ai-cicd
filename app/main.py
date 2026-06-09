from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input to prevent shell injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):  # Secure implementation using subprocess.run
    result = subprocess.run(['ping', safe_ping(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}