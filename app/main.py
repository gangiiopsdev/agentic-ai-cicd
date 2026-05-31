from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add your validation logic here to ensure the host parameter is safe
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise HTTPException(status_code=400, detail='Invalid host')

@app.get("/ping")
def ping(host: str):
    is_valid_host(host)
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}