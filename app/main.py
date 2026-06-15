from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.strip() or any(char in ' ;<>|&*?{}[]`$' for char in host):
        raise ValueError('Invalid host')
    args = ['ping', subprocess.DEVNULL, subprocess.STDOUT]
    subprocess.run(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)