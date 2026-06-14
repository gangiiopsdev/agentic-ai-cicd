from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(escape_host(host))
    # Secure implementation
    subprocess.call(['ping', '-c', '4', escaped_host])
    return {"status": "completed"}