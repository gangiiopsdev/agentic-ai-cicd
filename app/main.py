from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not validate_host(host):
        raise ValueError('Invalid host')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to use with ping
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False