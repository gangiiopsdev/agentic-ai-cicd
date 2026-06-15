from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}