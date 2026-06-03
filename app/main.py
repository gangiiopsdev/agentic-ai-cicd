from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host")
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_host(host))
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}