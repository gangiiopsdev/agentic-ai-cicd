from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.isalnum() and '.' in host

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}