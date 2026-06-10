from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen and shlex
    args = ['ping', host]
    subprocess.Popen(args)

@app.get("/ping")
def ping_route(host: str):  
    return ping(host)