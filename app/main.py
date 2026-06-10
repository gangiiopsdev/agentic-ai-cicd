from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        ip_address = subprocess.check_output(['hostname', '-i']).decode().strip()
        subprocess.run(['/sbin/ping', '-c', '1', ip_address], check=True, shell=False)
    except Exception as e:
        raise Exception(f'Ping failed: {e}')

@app.get('/ping')
def ping(host: str):
    if os.path.exists('/sbin/ping'):
        safe_ping(host)
    else:
        raise Exception('Ping executable not found')
    return {'status': 'completed'}