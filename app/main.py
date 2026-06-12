from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate and sanitize input
        if not host.isalnum():
            raise ValueError("Invalid hostname")
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping/{host}")
def ping_endpoint(host: str):
    return ping(host)