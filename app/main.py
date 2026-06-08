from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Full command and input validation
    if host.isnumeric() or '.' in host:
        sanitized_host = subprocess.shlex_quote(host)
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
    else:
        raise ValueError('Invalid host parameter')

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return ping(host)