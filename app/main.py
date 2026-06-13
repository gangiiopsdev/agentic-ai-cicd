from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_safe(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):    return {'status': 'completed'}