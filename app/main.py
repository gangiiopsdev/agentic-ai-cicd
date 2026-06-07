from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Define a list of allowed hosts or use whitelisting
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    import shlex
    safe_host = shlex.quote(host)
    return safe_ping(safe_host)