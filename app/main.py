from fastapi import FastAPI
import subprocess

app = FastAPI()

# Add validation logic for host here, e.g., whitelist allowed hosts
def is_valid_host(host):
    return host in ['example.com', 'test.com']

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'output': 'Invalid host'}, 400
    try:
        # Secure implementation using subprocess.run with shell=False and proper arguments
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}, 500