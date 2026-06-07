from fastapi import FastAPI
import subprocess
global ping_cmd
ping_cmd = ['ping', 'google.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['google.com']
    if host in allowed_hosts:
        try:
            subprocess.run(ping_cmd, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': f'Ping failed with error: {e}'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}