from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.run(['ping', escaped_host], check=True)  # Use subprocess.run to safely execute the command
    return {"status": "completed"}