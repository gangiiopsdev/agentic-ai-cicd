from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    subprocess.run(shlex.split(' '.join(args)), check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)