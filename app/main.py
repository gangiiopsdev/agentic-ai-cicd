from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def ping(host: str):
    # Regular expression to validate hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

# Additional recommendation: Use a more secure method for hostname validation if possible.
# Example: Validate against a list of allowed hosts or use DNS resolution to ensure the host exists.