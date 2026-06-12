from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    subprocess.call(command)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)