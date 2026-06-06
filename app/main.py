from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex.quote to safely escape the host parameter
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)