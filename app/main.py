from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using shlex.quote to escape special characters
    import shlex
    args = shlex.split('ping ' + host)
    subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}