from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@router.get('/ping')
def ping(host: str):
    # Enhanced security implementation with input validation and sanitization
    if not host.isdigit():
        return {'status': 'invalid_host'}
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}