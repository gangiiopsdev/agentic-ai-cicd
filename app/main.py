from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts
def execute_ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return execute_ping(host)