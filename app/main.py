from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    if not host or ' ' in host:
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', host])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = run_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return result
    return {'status': 'completed'}