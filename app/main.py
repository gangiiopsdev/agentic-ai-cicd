from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}