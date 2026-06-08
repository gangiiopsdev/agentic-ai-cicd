from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        command = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}