from fastapi import FastAPI
import subprocess
import re
global white_listed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in white_listed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}