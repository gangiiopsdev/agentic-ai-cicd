from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Define a set of allowed characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    # Check if all characters in the host are allowed
    return all(char in allowed_chars for char in host)

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host) or re.search(r'[^a-zA-Z0-9.-]', host):  # Enhanced validation
        return {'status': 'failed', 'error': 'Invalid host'}
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}