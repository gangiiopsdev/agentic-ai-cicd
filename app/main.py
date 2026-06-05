from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation to prevent shell injection
    if not host.isalnum() or '.' in host:
        return {'status': 'invalid input'}
    command = ['ping', host]
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}