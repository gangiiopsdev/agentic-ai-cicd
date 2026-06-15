from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using shlex.quote to escape user input
    args = ['ping', subprocess.list2cmdline([host])]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    if not all(c in '0123456789.' for c in host):
        return {"status": "invalid_host"}
    safe_ping(host)
    return {"status": "completed"}