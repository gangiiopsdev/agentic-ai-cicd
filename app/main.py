from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return shlex.quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    command = ['ping', escaped_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}