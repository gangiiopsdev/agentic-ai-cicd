from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric():
        # Use a list to avoid shell injection risks
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input for ping')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except ValueError as e:
        return {'error': str(e)}, 400