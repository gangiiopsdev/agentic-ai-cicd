from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if is_valid_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'success', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failure', 'error': e.stderr}
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

def is_valid_host(host: str) -> bool:
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))