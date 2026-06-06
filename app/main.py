from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # More secure implementation with regex to allow only valid hostnames
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}