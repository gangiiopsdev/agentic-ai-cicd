from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'invalid_host'}
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {'status': 'completed'}