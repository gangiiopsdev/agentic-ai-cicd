from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the input
    if not all(c.isalnum() or c in '.-@' for c in host):
        return {'status': 'error', 'result': 'Invalid host'}
    # Use shlex.quote to safely quote the command arguments
    quoted_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', quoted_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)