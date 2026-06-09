from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.strip().endswith('localhost') or '127.0.0.1' in host

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}