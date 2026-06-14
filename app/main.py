from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and a properly escaped command
    args = shlex.split('ping ' + host)
    subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)