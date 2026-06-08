from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return host.isalnum() and '-' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', '-c 1', subprocess.list2cmdline([host])]
    subprocess.run(command, check=True)
    return {'status': 'completed'}