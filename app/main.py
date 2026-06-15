from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation with input validation and quoting
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    sanitized_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': ping(host)}