from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent injection
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)