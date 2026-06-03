from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use a whitelist of allowed hosts to mitigate the risk of shell injection
        allowed_hosts = ['127.0.0.1', '::1']
        if host not in allowed_hosts:
            raise ValueError('Unauthorized host')
        command = shlex.split(f'ping {host}')
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}