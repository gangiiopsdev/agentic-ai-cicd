from fastapi import FastAPI
import subprocess
import re
generate_ping_command = lambda host: ['ping', host]
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Enhanced regex to validate the host name
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {'error': 'Invalid host name'}
    try:
        subprocess.call(generate_ping_command(host), shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}