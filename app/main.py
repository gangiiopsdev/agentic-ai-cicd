from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid input')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    validated_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', validated_host], check=True, capture_output=True, text=True)
    return {'host': host, 'output': result.stdout}