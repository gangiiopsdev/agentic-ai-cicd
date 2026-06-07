from fastapi import FastAPI
import shlex
import subprocess
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}
    args = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)