from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.isalnum():
        return False
    try:
        output = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host'}