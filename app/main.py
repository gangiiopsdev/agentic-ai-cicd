from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid or unsafe host provided")
    args = ['ping', '-c', '1'] + shlex.split(host)
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
    return output.decode()

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}