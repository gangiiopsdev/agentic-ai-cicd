from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip().isalnum():
        raise Exception('Invalid input for host')
    command = ["ping", *shlex.split(host)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed with error: {error.decode()}')

    return {'status': 'completed'}