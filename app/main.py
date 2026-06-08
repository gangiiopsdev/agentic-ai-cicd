from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
async def ping(host: str = Depends(validate_host)):
    try:
        # Use shlex.split to safely split the command into a list of arguments
        subprocess.run(shlex.split(f'ping {host}'), check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}