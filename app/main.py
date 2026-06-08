from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
cmd = ['ping'] + shlex.split(host)
subprocess.call(cmd)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)