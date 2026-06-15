from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    # Implement logic to check if the host is safe
    return host.isnumeric()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}