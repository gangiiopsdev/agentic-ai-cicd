from fastapi import FastAPI
import subprocess
def run_ping(host):
    if host and host.isnumeric():
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = run_ping(host)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'error': str(e)}