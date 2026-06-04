from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}