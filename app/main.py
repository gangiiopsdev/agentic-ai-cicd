from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def secure_ping(host: str):
    safe_host = quote(host.strip())
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    secure_ping(host)
    return {"status": "completed"}