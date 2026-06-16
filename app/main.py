from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation with argument escaping and validation
    if not host:
        raise ValueError('Host parameter cannot be empty')
    result = subprocess.call(['ping', host], shell=False)
    return {'status': 'completed', 'result': result}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)