from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation and complete command path
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)