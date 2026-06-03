from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid host name')
    # Use shlex.quote to safely quote the command argument
    cmd = ['ping', host]
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping(host: str):