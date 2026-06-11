from fastapi import FastAPI
import subprocess
from shlex import quote
from os.path import basename

app = FastAPI()

def validate_host(host: str):
    if not host or not basename(host).isalnum():
        raise ValueError("Invalid hostname")

def safe_subprocess_run(command: list):
    return subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping(host: str = Query(..., description="Hostname to ping")):
    try:
        validate_host(host)
        result = safe_subprocess_run(['ping', host])
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}