from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = ['host1', 'host2']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.call(['ping', '-c 1', host])  # Use '-c 1' to limit the number of pings
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}