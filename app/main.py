from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host):
    # Secure implementation using subprocess.run with args parameter and shell=False
    try:
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return execute_ping(host)

def is_valid_host(host):
    import re
    # Simple regex to validate host format
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None