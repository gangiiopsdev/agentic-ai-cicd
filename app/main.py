from fastapi import FastAPI
import subprocess
import re
def run_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = subprocess.list2cmdline([host])  # Sanitize the host input
    return run_ping(sanitized_host)
def validate_host(host: str) -> bool:
    # Add logic to validate the host here, e.g., check against a whitelist of allowed hosts
    pattern = re.compile(r'^\d+$')
    if not pattern.match(host):
        return False
    return True