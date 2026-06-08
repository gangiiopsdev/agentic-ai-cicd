from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Basic validation of the host
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None