from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}