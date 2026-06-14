from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    return all(c.isalnum() or c in [".", "-"] for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid hostname'}
    # Use a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Host not allowed'}