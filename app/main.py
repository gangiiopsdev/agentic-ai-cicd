from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', host]
    process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed'}
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)