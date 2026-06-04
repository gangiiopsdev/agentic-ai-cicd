from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)