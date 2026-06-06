from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex.quote to sanitize the input
    import shlex
    safe_host = shlex.quote(host)
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}