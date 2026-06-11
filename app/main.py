from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "message": "Invalid host name"}
    args = ['ping', subprocess.list2cmdline([host])]
    subprocess.run(args, check=True)
    return {"status": "completed"}