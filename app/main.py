from fastapi import FastAPI
import subprocess
import shlex

global host_whitelist
host_whitelist = ['google.com', 'example.com']  # Replace with actual allowed hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in host_whitelist:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        command = shlex.split(f'ping {host}')  # Use shlex to properly handle the input
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}