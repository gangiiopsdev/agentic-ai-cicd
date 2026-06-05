from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid host"}
    command = ['ping', '--'] + shlex.split(host)  # Use -- to prevent argument injection and shlex for safe splitting
    subprocess.call(command, shell=False)
    return {"status": "completed"}