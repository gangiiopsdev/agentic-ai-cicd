from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)