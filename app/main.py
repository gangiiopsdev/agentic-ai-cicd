from fastapi import FastAPI
import subprocess
import shlex
cimport re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    # Use shlex.quote to safely quote the command argument
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):