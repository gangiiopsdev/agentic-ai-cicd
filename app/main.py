from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input"}
    args = shlex.split(f"ping {shlex.quote(host)}")
    subprocess.call(args)
    return {"status": "completed"}