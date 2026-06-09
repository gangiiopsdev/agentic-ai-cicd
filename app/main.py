from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and validation of input
    if host.strip() == 'localhost':
        args = ['ping', host]
        subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)