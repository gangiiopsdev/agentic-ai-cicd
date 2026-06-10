from fastapi import FastAPI
import subprocess
cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    allowed_hosts = ['google.com', 'example.com']  # Add a whitelist of allowed hosts
    if host in allowed_hosts:
        command = ['ping', host]
        subprocess.run(command, check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}