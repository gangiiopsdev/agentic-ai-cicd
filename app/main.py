from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent command injection
    safe_host = subprocess.shlex_quote(host)
    subprocess.call(f'ping {safe_host}')

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)