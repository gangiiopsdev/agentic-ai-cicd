from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

def safe_ping(host):
    try:
        # Validate and sanitize the host input to avoid shell injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    # Implement validation logic here, e.g., allow only certain domain names
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail='Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}