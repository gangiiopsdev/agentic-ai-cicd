from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent injection
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_route(host: str):
    return ping(host)