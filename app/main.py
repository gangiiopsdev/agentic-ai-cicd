from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Full command and input validation
    if host.isnumeric() or '.' in host:
        sanitized_host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return result.returncode == 0
    else:
        raise ValueError('Invalid host parameter')

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)