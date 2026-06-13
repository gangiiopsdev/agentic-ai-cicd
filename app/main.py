from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and quoting
    if not host:
        raise ValueError('Host parameter is required')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}