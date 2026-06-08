from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    args = ['ping', '-c', '1', quote(host)]
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "result": result.stdout.decode()}
    else:
        return {"status": "failed", "result": result.stderr.decode()}