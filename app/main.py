from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not validate_host(host):
        raise ValueError('Invalid host')
    command = ['ping', '-c 1'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific domains or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts