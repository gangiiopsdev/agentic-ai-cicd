from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts or validate the input
        allowed_hosts = ['example.com', 'test.com']
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        command = ['ping', *shlex.split(host)]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)