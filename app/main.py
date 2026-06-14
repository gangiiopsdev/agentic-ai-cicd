from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}