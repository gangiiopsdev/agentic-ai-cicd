from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 64

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid input'}, 400
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}