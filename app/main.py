from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize host input to prevent command injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)