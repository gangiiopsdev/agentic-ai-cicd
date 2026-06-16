from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        return {"status": "failed", "error": "Invalid host name"}
    command = ['ping', shlex.quote(host)]
    try:
        subprocess.run(command, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "completed", "error": str(e)}
    return {"status": "completed"}