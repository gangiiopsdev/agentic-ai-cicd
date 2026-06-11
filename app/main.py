from fastapi import FastAPI
import subprocess
class ShellEscapeError(Exception):
    pass

def secure_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host")
    escaped_host = subprocess.list2cmdline([host])
    try:
        subprocess.call(['ping', escaped_host])
    except subprocess.CalledProcessError as e:
        raise ShellEscapeError(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}