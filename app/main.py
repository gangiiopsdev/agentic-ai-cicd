from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '192.168.1.1']  # Example allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
    else:
        return {'status': 'error', 'message': 'Invalid input'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict) and 'status' in result:
        return result
    else:
        return {'status': 'completed'}