from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with full path and input validation to prevent shell injection
    if not host or not host.isalnum():
        return {"status": "invalid host"}, 400
    command = ['/bin/ping'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {"status": "completed"}