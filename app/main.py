from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    return host

@app.get("/ping")
def ping(host: str):
    host = validate_host(host)
    command = ["ping", *shlex.split(host)]
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {"status": "completed", "output": result.stdout}