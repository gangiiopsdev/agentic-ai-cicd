from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    return host

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    args = ['ping', validated_host]
    subprocess.call(args)
    return {'status': 'completed'}