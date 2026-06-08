from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host to prevent malicious input
    if not is_valid_host(host):
        return {'status': 'invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Simple validation, improve as needed
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)