from fastapi import FastAPI
import subprocess
globally_safe_hosts = {'127.0.0.1', 'localhost'}

app = FastAPI()

def _ping(host):
    if host not in globally_safe_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    try:
        return _ping(host)
    except Exception as e:
        return {'error': str(e)}, 400

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}