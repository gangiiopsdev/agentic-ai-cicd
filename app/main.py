from fastapi import FastAPI
import subprocess
from os.path import expandvars

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with path expansion and input validation
    host = expandvars(host)
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', '-c', 1, host], check=True)
    return {'status': 'completed'}