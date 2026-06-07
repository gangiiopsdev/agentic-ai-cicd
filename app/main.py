from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result}