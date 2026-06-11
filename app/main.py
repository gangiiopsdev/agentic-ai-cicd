from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    command = ['ping', host]
    subprocess.run(command, check=True, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)