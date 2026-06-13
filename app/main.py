from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use shlex.quote to safely escape the user input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}