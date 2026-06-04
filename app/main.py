from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    # Regular expression to match a valid host name or IP address
    pattern = re.compile(r'^([a-zA-Z0-9.-]+)$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}