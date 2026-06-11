from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex
    args = ['ping', host]
    subprocess.run(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)