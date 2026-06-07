from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
def safe_ping(host):
    try:
        # Use a whitelist to validate host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host):
    # Implement validation logic here, e.g., checking if the host is in a predefined list
    return True
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)