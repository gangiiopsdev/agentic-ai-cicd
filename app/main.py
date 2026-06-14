from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)

    return {"status": "completed"}