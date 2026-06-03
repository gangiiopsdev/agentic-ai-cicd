from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Enhanced input validation to ensure it is a valid hostname
    if not re.match(r'^[a-zA-Z0-9-.]+$', host) or '.' not in host:
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)