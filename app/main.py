from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', '-c', '1', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}