from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Simple example of sanitization. Replace with more robust logic as needed.
    return ''.join(filter(str.isalnum, host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.call(args)
    return {'status': 'completed'}