from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)