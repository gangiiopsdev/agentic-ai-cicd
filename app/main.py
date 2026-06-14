from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()} 

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host) or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}

    # Further sanitize input to prevent command injection
    import re
    if re.match(r'^[a-zA-Z0-9-.]+$', host) is None or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid characters in hostname'}

    # Use shlex.quote to safely escape the input
    import shlex
    safe_host = shlex.quote(host)
    return SafePing.ping(safe_host)