from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}