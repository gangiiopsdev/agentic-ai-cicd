from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        output = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}