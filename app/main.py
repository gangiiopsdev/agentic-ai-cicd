from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Host not allowed'}
    args = shlex.split(f'ping -c 1 {host}')  # Limit ping to one packet for security
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}