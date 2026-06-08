from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    return host.replace('.', '').isalnum()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host name"}
    args = ['ping'] + [shlex.quote(host)]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}