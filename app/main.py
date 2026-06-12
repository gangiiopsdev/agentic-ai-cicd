from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'invalid_host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}