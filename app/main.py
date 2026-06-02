from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        print(f'Error pinging {host}: {e}')

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}