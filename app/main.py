from fastapi import FastAPI
import subprocess
import shlex
global allowed_hosts = {'example.com', '127.0.0.1'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"error": "Host not allowed"}
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}