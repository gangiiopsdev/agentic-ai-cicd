from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Validate input to prevent command injection
    if 'ping' not in host:
        raise ValueError('Invalid input')
    result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)