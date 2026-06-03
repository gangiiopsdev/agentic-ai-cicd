from fastapi import FastAPI
import subprocess
def run_ping(host):
    if not all(c.isalnum() or c in ['-', '_'] for c in host):
        raise ValueError('Invalid input')
    return subprocess.call(['ping', '-c', '1', host], shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = run_ping(host)
        return {'result': result}
    except ValueError as e:
        return {'error': str(e)}, 400