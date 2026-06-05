from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.strip().replace(' ', '').lower()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it's a safe hostname
    validated_host = validate_host(host)
    if not all(c.isalnum() or c in ['-', '.', '_', ','] for c in validated_host):
        raise ValueError('Invalid characters in host parameter')
    args = ['ping', validated_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}