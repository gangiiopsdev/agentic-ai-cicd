from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host parameter
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host format'}

    subprocess.call(['ping', host])

    return {'status': 'completed'}