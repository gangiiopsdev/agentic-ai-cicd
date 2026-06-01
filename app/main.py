from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate host input (e.g., allow only certain domains)
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com']
    for allowed_host in allowed_hosts:
        if host.endswith(allowed_host):
            return True
    return False