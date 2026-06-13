from fastapi import FastAPI, Depends
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['host1', 'host2']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return host

@app.get("/ping")
def ping(host: str = Depends(validate_host)):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}