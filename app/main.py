from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    # Escape any potentially harmful characters in host
    return ''.join(c for c in host if c.isalnum() or c in ['-', '.', '_'])

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    args = shlex.split(f'ping {escaped_host}')
    subprocess.call(args, shell=False)

    return {'status': 'completed'}