from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input to prevent command injection
    allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', '--no-privileged', host]
    result = subprocess.check_output(args, stderr=subprocess.STDOUT)
    return result
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except ValueError as e:
        return {'error': str(e)}