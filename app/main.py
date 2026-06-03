from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host parameter")
    # Using shlex.quote to safely escape the input
    import shlex
    subprocess.call(["ping", shlex.quote(host)])
    return {"status": "completed"}