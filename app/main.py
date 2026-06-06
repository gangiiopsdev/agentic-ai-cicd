from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate host input to ensure it's a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    command = ['ping', host]
    subprocess.call(command, shell=False)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}