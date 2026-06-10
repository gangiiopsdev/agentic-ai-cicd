from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid input')
    args = ['ping', '-c', '1', host]  # Limit ping to 1 packet for security
    result = await subprocess.run(shlex.split(' '.join(args)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

def ping(host: str):
    return safe_ping(host)