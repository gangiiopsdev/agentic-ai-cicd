from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.strip() or host.strip().isalnum():
        return True
    return False
app = FastAPI()
@app.get(
    "/ping",
    responses={400: {"model": str}}
)
def ping(host: str):
    if validate_host(host):
        command = ['ping'] + shlex.split(host)
        try:
            subprocess.run(command, check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}, 400
    else:
        return {"error": "Invalid host provided"}, 400