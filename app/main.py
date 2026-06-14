from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and proper use of subprocess
    valid_hosts = ['192.168.', '10.0.']
    for valid_host in valid_hosts:
        if host.startswith(valid_host):
            command = ['ping', host]
            subprocess.run(command, check=True)
            return {'status': 'completed'}
    return {'error': 'Invalid host'}