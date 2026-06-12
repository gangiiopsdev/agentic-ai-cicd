from fastapi import FastAPI
import subprocess
import shlex
from typing import Union
def safe_ping(host: str) -> Union[dict, None]:
    if not host.isalnum():
        return {'error': 'Invalid hostname'}
    command = ['ping', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)