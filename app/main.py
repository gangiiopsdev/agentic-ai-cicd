from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):

    # Secure implementation using shlex.quote for safe command construction
    subprocess.call(f"ping {quote(escape_host(host))}", shell=False)

    return {"status": "completed"}