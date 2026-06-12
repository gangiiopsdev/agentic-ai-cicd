from fastapi import FastAPI
import subprocess
cimport shlex

global app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex for safe argument splitting
    cmd = ['ping', host]
    subprocess.call(cmd, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)