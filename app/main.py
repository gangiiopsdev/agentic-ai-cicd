from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    args = shlex.split(f'ping {host}')
    process = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()
    if process.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed'}
    return {'status': 'success', 'output': result[0].decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)