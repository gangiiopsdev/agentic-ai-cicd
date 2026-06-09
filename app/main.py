from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input using a regular expression for more security
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):\n            return {'status': 'failed', 'error': 'Invalid host'}\
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)\
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': str(e)}

def is_valid_host(host: str) -> bool:
    # Basic validation logic for host
    return all(c.isalnum() or c in ['.', '-'] for c in host)