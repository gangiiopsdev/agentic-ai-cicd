from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or '.' in host:
        return False
    return True
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': f'Ping failed with error: {e.output}'}
    else:
        return {'error': 'Invalid host'}