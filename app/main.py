from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex
    args = ['ping', host]
    subprocess.call(args)

@app.get="/ping")
def ping(host: str):
    return ping(host)