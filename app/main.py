from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(e if e.isalnum() else '_' for e in host)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', escaped_host]
    subprocess.call(args)
    return {'status': 'completed'}