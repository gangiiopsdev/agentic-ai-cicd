from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        if safe_ping(host):
            output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        else:
            return {'status': 'failed', 'error': 'Unauthorized host'}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}