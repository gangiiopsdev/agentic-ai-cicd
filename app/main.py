from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return {'result': ping(host)}