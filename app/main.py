from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):,
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        output = subprocess.check_output([f'ping {host}'], shell=True, stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}