from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    args = ['ping', host]
    quoted_args = [shlex.quote(arg) for arg in args]
    try:
        output = subprocess.check_output(quoted_args, stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)