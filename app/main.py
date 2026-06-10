from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid_host"}

    # Use shlex.quote to safely include user input in the command
    import shlex
    safe_host = shlex.quote(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}