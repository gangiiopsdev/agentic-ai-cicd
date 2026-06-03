from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip() or not safe_ping(host):
        return {'error': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}