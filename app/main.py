from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex
    if not host.isalnum():
        return {'status': 'invalid input'}
    command_parts = ['ping', host]
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}