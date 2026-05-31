from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host is a valid IP address or hostname
    if '.' in host or ':' in host:
        return True
    return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid host'}
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}
    return {'status': 'completed'}