from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return shlex.quote(host)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}