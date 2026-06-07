from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    return host

def run_ping(host):
    args = shlex.split(f'ping -c 1 {host}')  # Limit the number of pings to mitigate potential abuse
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    try:
        response = run_ping(validated_host)
        return {'status': 'completed', 'response': response}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}