from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$', re.IGNORECASE)
    return bool(pattern.match(host))