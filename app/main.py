from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Use the built-in ping function instead of invoking shell
    import os
    if 'ping' in host:
        raise ValueError('Invalid hostname')
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)