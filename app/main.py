from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host or ' ' in host:
        return {"status": "invalid_host"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}