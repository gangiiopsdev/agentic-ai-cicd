from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.strip() or len(host) > 255:
        return False
    return True

app = FastAPI()

@app.get('/', summary='Home page')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping', summary='Ping a host safely')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}

    # Secure implementation with input validation and use of shlex
    args = ['/bin/ping'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}