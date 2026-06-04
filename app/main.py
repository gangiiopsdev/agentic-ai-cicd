from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Whitelisted hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)