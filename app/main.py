from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple regex to validate host
    import re
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}