from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

async def ping(host: str):
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

def ping_wrapper(host: str):
    return await ping(host)