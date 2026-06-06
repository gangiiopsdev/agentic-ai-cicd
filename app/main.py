from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_argument(value):
    return value.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    args = shlex.split(f'ping {escaped_host}')
    subprocess.call(args)
    return {"status": "completed"}