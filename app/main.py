from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}