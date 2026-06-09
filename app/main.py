from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(shlex.split(f'ping {host}'), check=True)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)