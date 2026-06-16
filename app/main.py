from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)