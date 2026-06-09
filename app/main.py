from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Simple validation of the host parameter
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {"status": "completed"}