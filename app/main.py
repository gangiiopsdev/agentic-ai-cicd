from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = quote(host)
    # Secure implementation
    subprocess.call(f"ping {escaped_host}")

    return {"status": "completed"}