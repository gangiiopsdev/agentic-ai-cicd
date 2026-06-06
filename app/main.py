from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate input to prevent shell injection attacks
    if '&&' in host or ';' in host:
        raise ValueError('Invalid input')
    try:
        output = subprocess.check_output(['ping', '-c', str(4), host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)