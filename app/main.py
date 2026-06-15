from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host input to avoid command injection
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    return result

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'status': safe_ping(host)}
    except Exception as e:
        return {'error': str(e)}, 400