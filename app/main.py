from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host):
    # Add validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts