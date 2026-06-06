from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        result = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}