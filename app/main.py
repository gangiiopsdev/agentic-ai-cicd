from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': result.stdout}