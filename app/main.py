from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command(input):
    return ''.join(c for c in input if c.isalnum() or c in ['-', '.', ':', '/'])

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command(host)
    args = shlex.split(f'ping -c 1 {safe_host}')
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}