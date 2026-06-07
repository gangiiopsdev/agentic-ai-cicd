from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    # Example validation logic, replace with actual validation
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}