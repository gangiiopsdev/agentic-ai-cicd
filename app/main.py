from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)