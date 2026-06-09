from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Implement your validation logic here (e.g., IP address pattern)
    return host.isdigit() and len(host) == 4

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    cmd_parts = ['ping', host]
    subprocess.call(cmd_parts, shell=False)
    return {'status': 'completed'}