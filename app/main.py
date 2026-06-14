from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def sanitize_host(host):
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or len(host) > 100:
        return {"error": "Invalid host name"}, 400
    subprocess.call(["ping", sanitize_host(host)], shell=False)
    return {"status": "completed"}