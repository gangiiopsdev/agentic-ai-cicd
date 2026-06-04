from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts

def is_valid_host(host):
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}