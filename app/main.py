from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').replace('-', '').isalnum()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}