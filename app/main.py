from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return run_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    return True