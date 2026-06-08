from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(host):
    # Add your sanitization logic here
    return host.strip()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = ['ping', quote(sanitized_host)]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}