from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def validate_host(host: str) -> Union[str, None]:
    # Add validation logic here to ensure host is safe
    return host if 'allowed_domains' in host else None

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    if validated_host:
        subprocess.call(['ping', validated_host])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}