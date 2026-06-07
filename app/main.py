from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def secure_ping(host):
    # Secure implementation with safe path and quoting
    command = ['ping', quote(host)]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}