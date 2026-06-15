from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)