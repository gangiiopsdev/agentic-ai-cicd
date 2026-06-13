from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')
app = FastAPI()
def execute_ping(host):    args = ['ping', host]    subprocess.run(args, check=True)
@app.get('/')def home():    return {'message': 'Agentic Self-Healing Pipeline'}@app.get('/ping')def ping(host: str):    validate_host(host)    execute_ping(host)    return {'status': 'completed'}