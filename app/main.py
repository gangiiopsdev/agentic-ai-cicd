from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e.stderr}')
        return False

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in the subprocess call
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'message': 'Invalid host'}
    if '..' in host.split('.'):
        return {'status': 'failed', 'message': 'Host contains invalid characters'}
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'message': 'Ping failed'}