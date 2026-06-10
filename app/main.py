from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname provided')
    command = shlex.split('ping ' + host)
    subprocess.run(command, check=True)
    return {'status': 'completed'}