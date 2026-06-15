from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}