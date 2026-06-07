from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = ''.join(c for c in host if c.isalnum() or c in '.:-')
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}