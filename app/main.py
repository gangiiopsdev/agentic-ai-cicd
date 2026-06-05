from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace("\", "\\")

app = FastAPI()

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    escaped_host = escape_host(host)
    subprocess.call(f"ping {escaped_host}", shell=False)

    return {status": "completed"}