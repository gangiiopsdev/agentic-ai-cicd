from fastapi import FastAPI
import re

app = FastAPI()

def safe_ping(host):
    # Validate host to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, shell=False, check=True)

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}