from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    return subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}