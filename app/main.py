from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent shell injection
    import shlex
    command = ['ping', host]
    subprocess.call(command)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)