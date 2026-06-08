from fastapi import FastAPI
import subprocess
get_shell = False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and all(c in string.digits for c in host) or 'localhost' in host:
        subprocess.call(['ping', host], shell=get_shell)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}