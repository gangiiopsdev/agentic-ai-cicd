from fastapi import FastAPI
import subprocess
from subprocess import TimeoutExpired
global allowed_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.check_output(['ping', f'"{host}"'], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except TimeoutExpired:
        return {'status': 'timeout', 'message': 'Operation timed out'}