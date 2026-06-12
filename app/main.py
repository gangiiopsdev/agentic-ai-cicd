from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host'}

    # Secure implementation
    subprocess.call(['ping', host], shell=False)

    return {'status': 'completed'}