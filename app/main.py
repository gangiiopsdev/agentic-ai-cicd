from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    command = ['ping', *shlex.split(host)]
    subprocess.run(command, check=True, capture_output=True)

@app.get('/ping')
async def ping(host: str):
    return {'status': safe_ping(host)}

def is_safe_host(host: str) -> bool:
    # Add logic to validate the host
    return True