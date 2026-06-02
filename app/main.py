from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def ping(host: str):
    try:
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host name")
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)