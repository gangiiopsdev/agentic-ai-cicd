from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}