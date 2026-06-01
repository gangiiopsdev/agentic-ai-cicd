from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if '.' in host:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'error': str(e)}