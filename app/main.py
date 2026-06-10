from fastapi import FastAPI
import subprocess

allowed_hosts = ['example.com', '192.168.0.1']

def safe_ping(host):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    try:
        output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}