from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')
    if not all(c in allowed_chars for c in host):
        return {'status': 'invalid_host'}
    args = shlex.split(f"ping {shlex.quote(host)}")
    subprocess.run(args, check=True)
    return {'status': 'completed'}