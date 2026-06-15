from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

# Add a function to validate the host input
import re
def is_valid_host(host: str) -> bool:
    pattern = r'^([a-zA-Z0-9.-]+)$'
    return re.match(pattern, host) is not None