from fastapi import FastAPI
import subprocess

app = FastAPI()

def _validate_host(host):
    if not host.replace('.', '', 3).isdigit():
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):
    try:
        _validate_host(host)
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}