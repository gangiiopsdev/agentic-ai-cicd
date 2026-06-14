from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Secure implementation
    args = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)