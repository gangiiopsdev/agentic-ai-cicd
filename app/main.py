from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not safe_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}