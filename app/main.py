from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate the host input to ensure it does not contain harmful characters or paths
    if not all(c.isalnum() for c in host) and not host.isdigit():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        subprocess.run(['ping', '-c 4', f'/sbin/ping {host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)