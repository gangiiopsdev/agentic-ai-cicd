from fastapi import FastAPI
import subprocess
generators = {
    'ping': lambda host: subprocess.call(['ping', host])
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in generators:
        generators[host](host)
    return {'status': 'completed'}