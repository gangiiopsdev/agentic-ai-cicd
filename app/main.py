from fastapi import FastAPI
import subprocess

app = FastAPI()

def create_ping_command(host):
    # Validate host to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    return ['ping', host]

@app.get('/ping')
def ping(host: str):
    subprocess.call(create_ping_command(host))
    return {'status': 'completed'}