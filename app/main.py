from fastapi import FastAPI
import subprocess
cimport os
def ping(host: str):
    try:
        if not host or len(host) > 255:
            raise ValueError("Invalid host")
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)