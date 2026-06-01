from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

# Function to validate and sanitize the host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex, allowed domain names)
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None