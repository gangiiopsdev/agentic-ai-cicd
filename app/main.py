from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if any(char in host for char in [';', '&', '|', '<', '>', '`']):
        raise ValueError('Unsafe input detected')
    subprocess.run(['ping', '-c', '1', subprocess.quote(host)], check=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}