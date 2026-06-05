from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=400, detail='Invalid host')
    return safe_ping(host)

def validate_host(host: str) -> bool:
    # Basic validation to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True