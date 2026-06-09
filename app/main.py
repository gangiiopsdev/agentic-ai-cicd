from fastapi import FastAPI
import subprocess32 as subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input using a whitelist approach
    allowed_networks = ['192.168.', '10.']
    if any(network.startswith(host) for network in allowed_networks):
        subprocess32.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}