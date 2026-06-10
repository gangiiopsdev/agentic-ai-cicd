from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '._-')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_host = escape_host(host)
    args = ['ping', safe_host]
    subprocess.call(args)
    return {'status': 'completed'}