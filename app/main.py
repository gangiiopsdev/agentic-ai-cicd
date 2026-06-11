from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to prevent shell injection
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)