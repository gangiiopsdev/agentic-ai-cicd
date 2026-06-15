from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['example.com', 'test.net']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_banned_hosts:
        return {'error': 'Host is not allowed'}, 403
    try:
        subprocess.call(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500