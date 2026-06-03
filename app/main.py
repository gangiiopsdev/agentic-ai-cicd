from fastapi import FastAPI
import shlex
def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid input')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}