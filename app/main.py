from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'error': 'Invalid input'}
    try:
        subprocess.run(safe_ping(host), check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}