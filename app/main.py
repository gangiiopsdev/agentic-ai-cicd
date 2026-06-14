from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
app = FastAPI()
@app.get('/ping')
def ping_safe(host: str):
    result = ping(host)
    return result