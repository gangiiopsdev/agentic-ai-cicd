from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {'status': 'failed', 'message': 'Invalid host'}
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return True  # Placeholder for actual validation