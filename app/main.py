from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = {'example.com', 'localhost'}

app = FastAPI()
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)