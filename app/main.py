from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.quote to safely escape host input
    subprocess.call(f'ping {shlex.quote(host)}')

@app.get("/ping")
def ping_endpoint(host: str):  
    return ping(host)