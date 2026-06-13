from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_host(host):
    # Define a safe list of hosts or use regex for validation
    pattern = r'^safehost1$|^safehost2$'
    return re.match(pattern, host) is not None

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        # Sanitize the input to avoid command injection
        sanitized_host = subprocess.quote(host)
        result = subprocess.run(['ping', '-c 1', sanitized_host], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}, 403