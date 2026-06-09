from fastapi import FastAPI
import subprocess
def run_safe_command(command, *args):
    safe_args = [arg for arg in args if isinstance(arg, str)]
    return subprocess.check_output([command] + safe_args, stderr=subprocess.STDOUT)

app = FastAPI()

@app.get('/ping')
def ping(host: str):