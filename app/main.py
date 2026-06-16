from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if 'ping' in host or '..' in host:
        raise ValueError('Invalid input')
    return host

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    subprocess.call(['ping', validated_host])
    return {'status': 'completed'}