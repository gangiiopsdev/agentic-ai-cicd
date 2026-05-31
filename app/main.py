from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    return subprocess.run(args, capture_output=True, text=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'output': result.stdout}