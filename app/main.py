from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}