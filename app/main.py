from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in host name')
    args = shlex.split(f'ping {shlex.quote(host)}')  # Use shlex.quote to properly escape the input
    subprocess.run(args, check=True)
    return {'status': 'completed'}