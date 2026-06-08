from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    return host.isdigit() and len(host) <= 15

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid host"}, 400
    args = ['ping', '-c', '1', shlex.quote(host)]
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}