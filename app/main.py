from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}