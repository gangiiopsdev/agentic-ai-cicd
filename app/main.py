from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safer implementation
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'success'}