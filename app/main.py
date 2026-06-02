from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input to ensure it is a valid hostname
    if not validate_hostname(host):
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

def validate_hostname(hostname: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9-.]+$')
    return bool(pattern.match(hostname))