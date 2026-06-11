from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com']  # List of allowed hosts
    if host in allowed_hosts:
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
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