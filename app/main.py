from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and shell=False
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed'}