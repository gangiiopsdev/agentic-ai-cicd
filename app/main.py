from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.strip() or len(host) > 255:
        return False, 'Invalid host name'
    try:
        output = subprocess.check_output(['ping', '-c', '1', '--', host], universal_newlines=True)
        return True, {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return False, {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    success, response = safe_ping(host)
    if not success:
        return response
    return response