from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use a whitelist for allowed hosts or perform additional validation
    if host not in ['allowed_host1', 'allowed_host2']:
        return {'status': 'failed', 'error': 'Invalid host'}
    safe_cmd = f'ping -c 1 {host}'
    try:
        output = subprocess.check_output(safe_cmd, stderr=subprocess.STDOUT, timeout=5, shell=True)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}