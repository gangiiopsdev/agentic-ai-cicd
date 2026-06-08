from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example whitelist of allowed hosts
    if not any(re.match(f'^{host}$', a) for a in allowed_hosts):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        args = shlex.split(f'ping {host}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}