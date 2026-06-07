from fastapi import FastAPI
import subprocess
gimport shlex
def escape_host(host: str):
    return shlex.quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}")
    return {"status": "completed"}