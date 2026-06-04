from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not host or ' ' in host:
        return {"status": "invalid_host"}

    # Sanitize the host input to prevent shell injection
    sanitized_host = shlex.quote(host)
    args = shlex.split(f"ping {sanitized_host}")
    subprocess.call(args)
    return {"status": "completed"}