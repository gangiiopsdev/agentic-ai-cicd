from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely escape host input
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it's safe
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_safe_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts