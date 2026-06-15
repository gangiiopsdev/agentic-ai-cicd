from fastapi import FastAPI
import subprocess
from shlex import quote
global os_path
os_path = '/bin/'

app = FastAPI()
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(host)  # Use shlex.quote to safely handle user input
    subprocess.run([os_path + 'ping', escaped_host], check=True)
    return {"status": "completed"}