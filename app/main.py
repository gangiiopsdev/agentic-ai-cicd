from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input')
    return ping(host)