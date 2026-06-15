from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        # Use a full path for the executable to avoid shell injection risks
        subprocess.run(['/bin/ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get('/ping')
def ping_safe(host: str):
    result = ping(host)
    return result