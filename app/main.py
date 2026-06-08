from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Simple check to ensure the host does not contain dangerous characters
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = shlex.split('ping ' + host)
    subprocess.call(args)
    return {"status": "completed"}