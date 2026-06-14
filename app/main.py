from fastapi import FastAPI
import subprocess
import shlex

def sanitize_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        return shlex.quote(host)
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        output = subprocess.check_output(['ping', sanitized_host], universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}