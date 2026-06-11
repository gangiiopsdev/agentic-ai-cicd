from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)