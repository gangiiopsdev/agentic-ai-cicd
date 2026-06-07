from fastapi import FastAPI
import subprocess
import re
def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)
def sanitize_input(input_str: str) -> str:
    sanitized_input = ''.join(c for c in input_str if c.isalnum() or c in '-.:')
    return sanitized_input
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):  # Validate the host input to prevent injection attacks
        raise ValueError('Invalid host name')
    sanitized_host = sanitize_input(host)
    args = ['ping', '-c', '1', sanitized_host]  # Limit the number of pings and use -c for compatibility
    subprocess.run(args, check=True, shell=False)  # Ensure shell=False to prevent shell injection
    return {'status': 'completed'}