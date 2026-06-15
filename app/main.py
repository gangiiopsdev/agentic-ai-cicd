from fastapi import FastAPI
import subprocess
cimport os
def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    env = os.environ.copy()
    result = subprocess.run(command, check=True, capture_output=True, text=True, env=env)
    return {'status': 'completed', 'output': result.stdout}