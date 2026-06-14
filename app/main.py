from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from shlex import quote

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping'], check=True, input=host.encode(), text=True)
    return JSONResponse(content={"status": "completed"})