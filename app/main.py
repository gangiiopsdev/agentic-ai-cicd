from fastapi import FastAPI
import re
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1'], capture_output=True, text=True, check=True, input=host)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}