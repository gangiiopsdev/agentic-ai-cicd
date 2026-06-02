from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_safe_command(command: str, args: list):
    safe_args = [quote(arg) for arg in args]
    subprocess.run([command] + safe_args, shell=False)

@app.get('/ping')
async def ping(host: str):
    run_safe_command('ping', [host])
    return {'status': 'completed'}