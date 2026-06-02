from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return host and len(host) <= 255

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}