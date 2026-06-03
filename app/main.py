from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        # Use a fully qualified command to avoid potential issues with the PATH environment variable
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.example.com']  # Add valid hosts here
    return host in allowed_hosts