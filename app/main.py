from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(host)  # Use shlex.quote to safely handle user input
    subprocess.run(['ping', escaped_host], check=True)
    return {"status": "completed"}