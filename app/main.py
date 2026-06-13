from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host and isinstance(host, str) and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return f'ping {host}'
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = safe_ping(host)
        subprocess.run(command, shell=True, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}