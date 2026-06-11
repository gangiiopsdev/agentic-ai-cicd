from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        cmd = ['ping', shlex.quote(host)]
        return subprocess.run(cmd, check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    return {'status': safe_ping(host)}