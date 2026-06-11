from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and shlex.split for safer command execution
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

def ping_wrapper(host: str):
    return await ping(host)